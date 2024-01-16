class Response:
    def __init__(self, response):
        self.response_full = response
        self.response_json = response.json()
        self.response_status = response.status_code
    
    def validate(self, schema):
        if isinstance(self.response_json, list):
            for item in self.response_json:
                schema.model_validate(item)
        else:
            schema.model_validate(self.response_json)
        return self
    
    def assert_status_code(self, status_code):
        assert self.response_status == status_code, self

    def __str__(self):
        return \
        f'\nStatus code: {self.response_status} \n' \
        f'Requested url: {self.response_full.url} \n' \
        f'Response body: {self.response_json} \n' \
        f'Response headers: {self.response_full.headers}'