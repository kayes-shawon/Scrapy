from django.contrib.postgres.indexes import BrinIndex
from django.db import models
from django.utils import timezone
from django.db.models import Manager


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

    def __str__(self):
        return f'id: {self.id} url: {self.scrape_url}'

    class Meta:
        db_table = 'product_image'
        indexes = [
            BrinIndex(fields=['updated_at'], name='product_image_updated_at_bri'),
            BrinIndex(fields=['created_at'], name='product_image_created_at_bri'),
        ]

        verbose_name = 'Product Image'
        verbose_name_plural = 'Product Image'
