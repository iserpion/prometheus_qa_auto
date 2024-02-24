import pytest
from modules.common.schemas.pet import Pet
from modules.common.data.pet_data import PetData
from http import HTTPStatus


# Positive test cases:

@pytest.mark.rest_api
def test_create_new_pet(petstore_api, pet_validate):
    """Test checks creating a new pet"""

    response = petstore_api.create_new_pet(
        PetData.post_pet_headers, 
        PetData.post_pet_body
    )
    pet_validate.validate(response, Pet)

    assert response.status_code == HTTPStatus.OK
    assert response.json() == PetData.post_pet_body


@pytest.mark.rest_api
def test_find_pet_by_id(petstore_api, pet_validate):
    """Test checks retrieving pet by id"""

    response = petstore_api.get_pet_by_id(
        PetData.PET_ID, 
        PetData.get_pet_headers
    )
    pet_validate.validate(response, Pet)

    assert response.status_code == HTTPStatus.OK
    assert response.json() == PetData.post_pet_body


@pytest.mark.rest_api
def test_update_pet(petstore_api, pet_validate):
    """Test checks updating pet"""

    response = petstore_api.update_pet(
        PetData.post_pet_headers, 
        PetData.put_pet_body
    )
    pet_validate.validate(response, Pet)

    assert response.status_code == HTTPStatus.OK
    assert response.json() == PetData.put_pet_body


@pytest.mark.rest_api
def test_delete_pet(petstore_api):
    """Test checks deleting pet"""

    response_del = petstore_api.delete_pet(PetData.PET_ID)
    response_get = petstore_api.get_pet_by_id(PetData.PET_ID)

    assert response_del.status_code == HTTPStatus.OK
    assert response_del.text == PetData.PET_DELETED_TEXT
    assert response_get.status_code == HTTPStatus.NOT_FOUND
    assert response_get.text == PetData.PET_NOT_FOUND_TEXT


# Negative test cases:

@pytest.mark.rest_api
def test_create_new_pet_negative(petstore_api):
    """Test checks attempt to create pet w/o id in request"""

    payload = PetData.post_pet_body.copy()
    payload.pop("id")

    response = petstore_api.create_new_pet(PetData.post_pet_headers, payload)
    response_body = response.json()

    assert response.status_code == HTTPStatus.INTERNAL_SERVER_ERROR
    assert response_body["code"] == HTTPStatus.INTERNAL_SERVER_ERROR
    assert PetData.POST_ERR_MESSAGE in response_body["message"]


@pytest.mark.rest_api
def test_find_pet_negative(petstore_api):
    """Test checks attempt to request pet with invalid id"""

    response = petstore_api.get_pet_by_id(
        PetData.INVALID_PET_ID, 
        PetData.get_pet_headers
    )
    response_body = response.json()

    assert response.status_code == HTTPStatus.BAD_REQUEST
    assert response_body["code"] == HTTPStatus.BAD_REQUEST
    assert response_body["message"] == PetData.ERR_MESSAGE


@pytest.mark.rest_api
def test_update_pet_negative(petstore_api):
    """Test checks attempt to update pet w/o name in request"""

    payload = PetData.put_pet_body.copy()
    payload.pop("name")
    response = petstore_api.update_pet(PetData.post_pet_headers, payload)

    assert response.status_code == HTTPStatus.NOT_FOUND
    assert response.text == PetData.PET_NOT_FOUND_TEXT


@pytest.mark.rest_api
def test_delete_pet_negative(petstore_api):
    """Test checks attempt to delete pet with invalid id in request"""

    response = petstore_api.delete_pet(PetData.INVALID_PET_ID)
    response_body = response.json()

    assert response.status_code == HTTPStatus.BAD_REQUEST
    assert response_body["code"] == HTTPStatus.BAD_REQUEST
    assert response_body["message"] == PetData.ERR_MESSAGE
