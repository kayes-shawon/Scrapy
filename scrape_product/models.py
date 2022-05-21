from django.db import models

# Create your models here.
from django.db.models import Manager
from django.utils import timezone


class ProductImageManager(Manager):
    pass


class ProductImage(models.Model):
    """
    Product image model
    """
    id = models.CharField(max_length=26, primary_key=True, verbose_name="id")
    scrape_url = models.CharField(max_length=250, verbose_name='Scrape url')
    original_size = models.CharField(max_length=100, verbose_name='Original size')
    alt_data = models.CharField(max_length=100, verbose_name='Alt data')
    updated_at = models.DateTimeField(default=timezone.now,
                                      verbose_name='Updated at')
    created_at = models.DateTimeField(default=timezone.now,
                                      verbose_name='Created at')

    objects = ProductImageManager()

    def save(self, *args, **kwargs):
        self.updated_at = timezone.now()
        super(ProductImage, self).save(*args, **kwargs)
