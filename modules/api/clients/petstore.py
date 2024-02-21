import requests


class PetStore:
    """Class holds methods for interacting with Swagger PetStore API"""

    base_url = 'https://petstore3.swagger.io/api/v3'

    def create_new_pet(self, headers_, payload):
        response = requests.post(
            self.base_url+'/pet', 
            headers=headers_, 
            json=payload
        )

        return response
    
    def get_pet_by_id(self, pet_id, headers_ = None):
        response = requests.get(
            self.base_url+f'/pet/{pet_id}', 
            headers=headers_
        )

        return response
        
    def update_pet(self, headers_, payload):
        response = requests.put(
            self.base_url+'/pet', 
            headers=headers_, 
            json=payload
        )

        return response
            
    def delete_pet(self, pet_id):
        response = requests.delete(self.base_url+f'/pet/{pet_id}')

        return response
    