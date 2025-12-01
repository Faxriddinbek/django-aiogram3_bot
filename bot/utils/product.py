from asgiref.sync import sync_to_async

from bot.models.product import Product


@sync_to_async
def get_product_by_title(title: str):
    return Product.objects.filter(title__iexact=title).first()


@sync_to_async
def get_sets_products(status=True):
    """Get all Sets category products from database"""
    return list(Product.objects.filter(
        category__title='🍱 Setlar',
        status=status
    ))

@sync_to_async
def get_snacks_products(status=True):
    """Get all Sets category products from database"""
    return list(Product.objects.filter(
        category__title="🍟 Sneklar",
        status=status
    ))


@sync_to_async
def get_burgerlar_products(status=True):
    """Get all Sets category products from database"""
    return list(Product.objects.filter(
        category__title="🍔 Burgerlar",
        status=status
    ))

@sync_to_async
def get_tovuq_products(status=True):
    """Get all Sets category products from database"""
    return list(Product.objects.filter(
        category__title="🍗 Tovuq",
        status=status
    ))

@sync_to_async
def get_lesterlar_products(status=True):
    """Get all Sets category products from database"""
    return list(Product.objects.filter(
        category__title="🌯 Lesterlar",
        status=status
    ))

@sync_to_async
def get_hot_dog_products(status=True):
    """Get all Sets category products from database"""
    return list(Product.objects.filter(
        category__title="🌭 Longerlar/Hot-dog",
        status=status
    ))

