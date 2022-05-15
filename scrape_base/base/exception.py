class CodeObjectException(Exception):
    def __init__(self, **kwargs):
        params = kwargs.get("params", {})

        if len(params) != 0:
            self.code_object = kwargs.get('code_object').deep_copy()
        else:
            self.code_object = kwargs.get('code_object')

    def get_code_object(self):
        return self.code_object
