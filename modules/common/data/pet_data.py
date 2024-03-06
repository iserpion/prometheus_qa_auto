from modules.common.data.enums import PetStatus


class PetData:
    PET_ID = 1111
    INVALID_PET_ID = 'pet_id'
    PET_DELETED_TEXT = 'Pet deleted'
    PET_NOT_FOUND_TEXT = 'Pet not found'
    ERR_MESSAGE = (
        "Input error: couldn't convert `pet_id` to type `class java.lang.Long`"
    )
    POST_ERR_MESSAGE = 'There was an error processing your request.'

    post_pet_headers = {
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }

    get_pet_headers = {
        'Accept': 'application/json',
    }

    post_pet_body = {
        'id': PET_ID,
        'name': 'kota',
        'photoUrls': [
            'https://pet-photos.com/some-pet1.img',
        ],
        'category': {
            'id': 1111,
            'name': 'some-category'
        },
        'tags': [
            {
                'id': 2222,
                'name': 'some-tag1'
            }
        ],
        'status': PetStatus.pending
    }

    put_pet_body = {
        'id': PET_ID,
        'name': 'kota',
        'photoUrls': [
            'https://pet-photos.com/some-pet1.img',
            'https://pet-photos.com/some-pet2.img',
        ],
        'category': {
            'id': 1111,
            'name': 'some-category'
        },
        'tags': [
            {
                'id': 2222,
                'name': 'some-tag1'
            },
            {
                'id': 3333,
                'name': 'some-tag2'
            }
        ],
        'status': PetStatus.sold
    }
