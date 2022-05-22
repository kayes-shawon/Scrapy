import pytz
import datetime

from django.core.exceptions import ObjectDoesNotExist
from django.utils.timezone import get_current_timezone

from scrape_base.base.api import BaseGetAPI
from scrape_base.base.exception import CodeObjectException
from scrape_product.code import product as product_code
from scrape_product.models import ProductImage


class ProductDetailsAPI(BaseGetAPI):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def api_version(self) -> str:
        return 'v1'

    def api_name(self) -> str:
        return 'ProductDetailsAPI'

    def process(self) -> tuple:
        payload = self.api_payload()
        image_id = payload.get('image_id', None)

        original_url = payload.get('original_url', None)
        scrape_date = payload.get('scrape_date', None)

        if image_id:
            try:
                product = ProductImage.objects.get(id=int(image_id))
            except ObjectDoesNotExist:
                raise CodeObjectException(code_object=product_code.PRODUCT_DOES_NOT_EXIST)

            data = {
                'image_id': product.id,
                'original_url': product.original_url,
                'scrape_url': product.scrape_url,
                'alt_data': product.alt_data,
                'product_url': product.product_url,
                'created_at': str(product.created_at)
            }
            return product_code.REQUEST_SUCCESSFUL, data

        elif original_url:
            query = ProductImage.objects.filter(scrape_url=original_url)
            product_list = ProductImage.objects.get_products(query)

            data = {
                'product_list': product_list
            }
            return product_code.REQUEST_SUCCESSFUL, data

        elif scrape_date:
            start_date = datetime.datetime.strptime(scrape_date, '%Y-%m-%d').date()

            date_min = datetime.datetime.combine(start_date, datetime.time.min,
                                                 tzinfo=get_current_timezone())

            date_max = datetime.datetime.combine(start_date + datetime.timedelta(days=1), datetime.time.min,
                                                 tzinfo=get_current_timezone())

            query = ProductImage.objects.filter(
                created_at__range=(date_min.astimezone(pytz.UTC), date_max.astimezone(pytz.UTC))
            )
            product_list = ProductImage.objects.get_products(query)
            data = {
                'product_list': product_list
            }
            return product_code.REQUEST_SUCCESSFUL, data

        else:
            raise CodeObjectException(code_object=product_code.NO_QUERY_PROVIDED)


