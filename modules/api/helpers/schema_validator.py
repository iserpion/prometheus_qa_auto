import pytest


class SchemaValidator:
    """Class holds method for validating response body schema"""
   
    def validate(self, response, schema):
        self.response_json = response.json()

        try: 
            if isinstance(self.response_json, list):
                for item in self.response_json:
                    schema.model_validate(item)
            else:
                schema.model_validate(self.response_json)
        except ValueError as e:
            pytest.fail(str(e))

    