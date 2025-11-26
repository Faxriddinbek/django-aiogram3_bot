from typing import Callable, Dict, Any, Awaitable

from aiogram import BaseMiddleware
from aiogram.types import Message, CallbackQuery
from django.utils.translation import activate

from bot.utils.translation import get_user_language


class TranslationMiddleware(BaseMiddleware):# dodim custom midlevere yozsa BaseMiddleware danchaqiriladi
    """Middleware to automatically set user's language for each update"""

    async def __call__(
            self,
            handler: Callable[[Message, Dict[str, Any]], Awaitable[Any]],# hamma midleverda hendler hcaqiriladi
            event: Message | CallbackQuery,# bu hendler Inlineda ishlaydi
            data: Dict[str, Any]
    ) -> Any:
        # Get user_id from the event
        user_id = event.from_user.id# eventdan userni id sini olish kerak

        # Activate user's language (await the async function)
        language = await get_user_language(user_id)# user tili
        activate(language)# activate djangodagi ficher _ tilni berilsa (_) ishlayudi

        # Add translation info to data
        data['user_language'] = language # bu dataga add (keyinchalik kerak bo'ladi)

        # Call the handler
        return await handler(event, data)