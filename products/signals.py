from django.core.cache import cache
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from .models import Product

def invalidate_products_cache(sender, **kwargs):
    cache.delete('products_list')

receiver(post_save, sender=Product)(invalidate_products_cache)
receiver(post_delete, sender=Product)(invalidate_products_cache)