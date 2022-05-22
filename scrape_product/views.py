from scrape_base.views.base import BasePostAPIView, BaseGetAPIView
from scrape_product.product.details import ProductDetailsAPI
from scrape_product.product.product import ScrapeProductAPI
from scrape_product.serializers.product import ScrapeProductInputSerializer


class ScrapeProductAPIView(BasePostAPIView):
    api_class = ScrapeProductAPI
    serializer_class = ScrapeProductInputSerializer
    disable_serializer_class = False

    def __str__(self):
        return 'ScrapeProductAPIView'


class ProductDetailsAPIView(BaseGetAPIView):
    serializer_class = None
    disable_serializer_class = True
    api_class = ProductDetailsAPI

    def __str__(self):
        return 'ProductDetailsAPIView'
