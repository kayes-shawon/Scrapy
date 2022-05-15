import logging
import abc

logger = logging.getLogger(__name__)


class BasePostAPI(abc.ABC):
    def __init__(self, **kwargs):
        super(BasePostAPI, self).__init__()
        self._version = kwargs.get('version', 'v1')
        self._view = kwargs.get('view', None)
        self._request = kwargs.get('request', None)

        self._api_payload = {}

    def set_api_payload(self, ap: dict):
        self._api_payload = ap

    def api_payload(self):
        return self._api_payload

    def version(self):
        return self._version

    def view(self):
        return self._view

    def request(self):
        return self._request

    @classmethod
    def api(cls, api_payload: dict, **kwargs) -> tuple:
        _api = cls(**kwargs)
        logger.debug(f'API Name: {_api.api_name()} API Version: {_api.api_version()}')
        logger.debug(f'kwargs: {kwargs}')
        _api.set_api_payload(api_payload)
        return _api.process()

    @abc.abstractmethod
    def process(self) -> tuple:
        pass

    @abc.abstractmethod
    def api_name(self) -> str:
        pass

    @abc.abstractmethod
    def api_version(self) -> str:
        pass


class BaseGetAPI(BasePostAPI, abc.ABC):
    pass
