import logging

from django.conf import settings

from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView

from scrape_base.base.exception import CodeObjectException
from scrape_base.base.utils import formatted_output_error, formatted_output_success
from scrape_base.code import base as base_codes

logger = logging.getLogger(__name__)

# def response_maker(cls, input_data, request):
#     try:
#         api_payload = cls.pre_process(input_data)
#         api_output = cls.api_class.api(api_payload,
#                                        view=cls,
#                                        request=request)
#
#         output = formatted_output_success(api_output[0], api_output[1])
#         logger.debug(output)
#         return Response(**output)
#     except CodeObjectException as e:
#         output = formatted_output_error(e.get_code_object())
#         logger.debug(output)
#         return Response(**output)
#     except Exception as e:
#         if settings.DEBUG:
#             logger.exception(e)
#         else:
#             logger.error(e)
#         output = formatted_output_error(base_codes.UNEXPECTED_ERROR)
#         logger.debug(output)
#         return Response(**output)


class BasePostAPIView(APIView):
    version = 'v1'
    api_class = None
    serializer_class = None
    disable_serializer_class = False

    def __str__(self) -> str:
        return 'BasePostAPIView'

    def pre_process(self, api_payload: dict) -> dict:
        """
        Pre process data here before sending it to api_class
        Make sure not to raise any exception

        :param api_payload:
        :return:
        """
        logger.debug(f'{self}: pre processing data')
        return api_payload

    def post(self, request: Request) -> Response:
        logger.debug(f' APIView: {self} URL: {request.get_full_path()}')
        input_data = request.data

        if self.disable_serializer_class:
            logger.debug('Serializer class disabled')
        else:
            logger.debug(f" serializing request data...")
            serializer = self.serializer_class(data=request.data)
            if not serializer.is_valid():
                logger.error(serializer.errors)
                output = formatted_output_error(base_codes.IMPROPER_DATA_FORMAT)
                logger.debug(output)
                return Response(**output)
            input_data = serializer.validated_data

        try:
            # TODO: Replace Repeated code
            api_payload = self.pre_process(input_data)
            api_output = self.api_class.api(api_payload,
                                            view=self,
                                            request=request)

            output = formatted_output_success(api_output[0], api_output[1])
            logger.debug(output)
            return Response(**output)
        except CodeObjectException as e:
            output = formatted_output_error(e.get_code_object())
            logger.debug(output)
            return Response(**output)
        except Exception as e:
            if settings.DEBUG:
                logger.exception(e)
            else:
                logger.error(e)
            output = formatted_output_error(base_codes.UNEXPECTED_ERROR)
            logger.debug(output)
            return Response(**output)


class BaseGetAPIView(APIView):
    version = 'v1'
    api_class = None
    serializer_class = None
    disable_serializer_class = False

    def __str__(self) -> str:
        return 'BaseGetAPIView'

    def pre_process(self, api_payload: dict) -> dict:
        """
        Pre process data here before sending it to api_class
        Make sure not to raise any exception

        :param api_payload:
        :return:
        """
        logger.debug(f'{self}: pre processing data')
        return api_payload

    def get(self, request: Request, **kwargs) -> Response:
        logger.debug(f' APIView: {self} URL: {request.get_full_path()}')

        input_data = kwargs
        for i in request.query_params:
            if len(request.query_params[i]) == 1:
                input_data[i] = request.query_params[i][0]
            else:
                input_data[i] = request.query_params[i]

        if not self.disable_serializer_class:
            serializer = self.serializer_class(data=input_data)
            if not serializer.is_valid():
                logger.error(serializer.errors)
                output = formatted_output_error(base_codes.IMPROPER_DATA_FORMAT)
                logger.debug(output)
                return Response(**output)
            input_data = serializer.validated_data

        try:
            api_payload = self.pre_process(input_data)
            api_output = self.api_class.api(api_payload,
                                            view=self,
                                            request=request)
            output = formatted_output_success(api_output[0], api_output[1])
            logger.debug(output)
            return Response(**output)
        except CodeObjectException as e:
            output = formatted_output_error(e.get_code_object())
            logger.debug(output)
            return Response(**output)
        except Exception as e:
            if settings.DEBUG:
                logger.exception(e)
            else:
                logger.error(e)
            output = formatted_output_error(base_codes.UNEXPECTED_ERROR)
            logger.debug(output)
            return Response(**output)
