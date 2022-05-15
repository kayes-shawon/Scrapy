from scrape_base.views.base import BasePostAPIView
from scrape_product.product.product import ScrapeProductAPI
from scrape_product.serializers.product import ScrapeProductInputSerializer


class ScrapeProductAPIView(BasePostAPIView):
    api_class = ScrapeProductAPI
    serializer_class = ScrapeProductInputSerializer
    disable_serializer_class = False
