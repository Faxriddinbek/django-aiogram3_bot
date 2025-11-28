from asgiref.sync import sync_to_async

from bot.models.product import Category


@sync_to_async
def get_all_category():
    """Get all Category from database"""
    return list(Category.objects.all())