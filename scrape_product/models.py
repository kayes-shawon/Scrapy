from django.contrib.postgres.indexes import BrinIndex
from django.db import models
from django.utils import timezone
from django.db.models import Manager


class ProductImageManager(Manager):
    def create_product(self, **kwargs):
        return self.create(
            scrape_url=kwargs.get('url'),
            original_size=kwargs.get('image_size'),
            alt_data=kwargs.get('alt', ''),
        )

    @staticmethod
    def get_products(request_data) -> list:
        output = []
        for p in request_data:
            product_dict = dict()
            product_dict['image_id'] = p.id
            product_dict['original_url'] = p.original_url
            product_dict['scrape_url'] = p.scrape_url
            product_dict['alt_data'] = p.alt_data
            product_dict['product_url'] = p.product_url
            output.append(product_dict)
        return output


class ProductImage(models.Model):
    """
    Product image model
    """
    id = models.BigAutoField(primary_key=True, verbose_name="Product Id")
    original_url = models.CharField(max_length=250, default="", verbose_name='Original url')
    scrape_url = models.CharField(max_length=250, default="", verbose_name='Scrape url')
    product_url = models.CharField(max_length=250, default="", verbose_name='Product url')
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
