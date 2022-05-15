class CodeObject(object):
    def __init__(self, **kwargs):
        self._http_status = kwargs.get('http_status', 500)
        self._state_code = kwargs.get('state_code', 'SCRAPE_BASE_CO_500')

    def http_status(self) -> int:
        return self._http_status

    def set_http_status(self, status):
        self._http_status = status

    def state_code(self) -> str:
        return self._state_code

    def set_state_code(self, state_code):
        self._state_code = state_code

    def is_http_error_status(self) -> bool:
        return 400 <= self._http_status <= 599

    def is_http_success_status(self) -> bool:
        return 200 <= self._http_status <= 299

    def deep_copy(self):
        return CodeObject(
            http_status=self.http_status(),
            state_code=self.state_code()
        )

