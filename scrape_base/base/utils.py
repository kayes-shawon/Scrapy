from django.utils.translation import get_language_from_request

from .code import CodeObject


def http_status_code(code: CodeObject) -> int:
    return code.http_status()


def state_code(code: CodeObject) -> str:
    return code.state_code()


def formatted_output_error(code: CodeObject) -> dict:
    if not code.is_http_error_status():
        raise ValueError('the http status code is not in error range')
    output = dict()
    output['status'] = http_status_code(code)
    output['data'] = {}
    output['data']['code'] = state_code(code)
    return output


def formatted_output_success(code: CodeObject, data: dict) -> dict:
    if not code.is_http_success_status():
        raise ValueError('the http status code is not in success range')
    output = dict()
    output['status'] = http_status_code(code)
    output['data'] = {}
    output['data']['code'] = state_code(code)
    output['data']['data'] = data
    return output


def get_language(request) -> str:
    return get_language_from_request(request)
