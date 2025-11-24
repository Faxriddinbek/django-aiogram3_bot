import json
import logging

from aiogram.types import Update  # telegramdan keladigon har bir habarni yangilish
from django.http import JsonResponse # django json formatta javob qaytarish uchun
from django.views.decorators.csrf import csrf_exempt # srf tokenni o'chirish
from django.views.decorators.http import require_POST

from bot.apps import BotConfig # AppConfig ichida bot va dispatcher saqlangan joy

logger = logging.getLogger(__name__)

"""
Webhook function
"""

@csrf_exempt # bu dekorator telegram wephuk shu yerga so'rov jo'natadi
@require_POST #faqat post so'rovini qabul qiladi
async def webhook(request):
    """
    Async webhook endpoint for receiving Telegram updates
    """
    try:
        update_data = json.loads(request.body.decode('utf-8'))# telegram yuborgan json xabarni python dictga aylantiradi
        update = Update(**update_data)#aiogram update obyektiga aylanadi

        # Process update with registered handlers
        await BotConfig.dp.feed_update(bot=BotConfig.bot, update=update) # kelgan habarni update qiladi

        return JsonResponse({'status': 'ok'})# telegramga ok deb javob beradi

    except Exception as e:# hatolarni loga yozadi va 500 qaytaradi
        logger.error(f"Webhook error: {e}", exc_info=True)
        return JsonResponse({'status': 'error', 'message': str(e)}, status=500)


async def set_webhook_view(request):
    """Set webhook URL"""
    from core import config

    try:
        webhook_url = f"{config.BASE_WEBHOOK_URL}{config.WEBHOOK_PATH}"
        await BotConfig.bot.set_webhook(
            url=webhook_url,
            secret_token=config.WEBHOOK_SECRET,
            drop_pending_updates=True
        )

        webhook_info = await BotConfig.bot.get_webhook_info()

        return JsonResponse({
            'status': 'success',
            'message': f'Webhook set to: {webhook_url}',
            'webhook_info': {
                'url': webhook_info.url,
                'pending_update_count': webhook_info.pending_update_count
            }
        })

    except Exception as e:
        logger.error(f"Set webhook error: {e}", exc_info=True)
        return JsonResponse({'status': 'error', 'message': str(e)}, status=500)


async def webhook_info_view(request):
    """Get webhook info"""
    try:
        webhook_info = await BotConfig.bot.get_webhook_info()

        return JsonResponse({
            'status': 'success',
            'webhook_info': {
                'url': webhook_info.url,
                'has_custom_certificate': webhook_info.has_custom_certificate,
                'pending_update_count': webhook_info.pending_update_count,
                'last_error_date': webhook_info.last_error_date,
                'last_error_message': webhook_info.last_error_message,
                'max_connections': webhook_info.max_connections,
            }
        })

    except Exception as e:
        logger.error(f"Webhook info error: {e}", exc_info=True)
        return JsonResponse({'status': 'error', 'message': str(e)}, status=500)


def health_check(request):
    """Health check endpoint"""
    return JsonResponse({'status': 'ok'})