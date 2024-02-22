import pytest
from http import HTTPStatus
from modules.common.data.spacex_data import SpaceXData


# Positive test cases:

@pytest.mark.gql_api
def test_get_company_info(spacex_api, spacex_query):
    """Test verifies retrieving SpaceX company info"""

    spacex_query.company()
    response = spacex_api.send_qraphql_query(spacex_query)

    assert response.status_code == HTTPStatus.OK
    assert response.json() == SpaceXData.company_data


@pytest.mark.gql_api
def test_get_history(spacex_api, spacex_query):
    """Test verifies retrieving SpaceX history episode"""
    
    spacex_query.history(id = SpaceXData.history_id)
    response = spacex_api.send_qraphql_query(spacex_query)

    assert response.status_code == HTTPStatus.OK
    assert response.json() == SpaceXData.history_data


@pytest.mark.gql_api
def test_get_rocket_info(spacex_api, spacex_query):
    """Test verifies retrieving SpaceX rocket info"""
    
    spacex_query.rocket(id = SpaceXData.rocket_id)
    response = spacex_api.send_qraphql_query(spacex_query)

    assert response.status_code == HTTPStatus.OK
    assert response.json() == SpaceXData.rocket_data


# Negative test cases:

@pytest.mark.gql_api
def test_get_company_info_negative(spacex_api, spacex_query):
    """
    Test verifies attempt to retrieve 
    SpaceX company info using invalid query data
    """

    spacex_query.company_bad()
    response = spacex_api.send_qraphql_query(spacex_query)

    assert response.status_code == HTTPStatus.BAD_REQUEST
    assert (
        response.json()['errors'][0]['extensions']['code'] == SpaceXData.error_text
    )
    

@pytest.mark.gql_api
def test_get_history_negative(spacex_api, spacex_query):
    """
    Test verifies attempt to retrieve 
    SpaceX history episode not providing required parameter
    """
    
    spacex_query.history()
    response = spacex_api.send_qraphql_query(spacex_query)

    assert response.status_code == HTTPStatus.BAD_REQUEST
    assert (
        response.json()['errors'][0]['extensions']['code'] == SpaceXData.error_text
    )


@pytest.mark.gql_api
def test_get_rocket_info_negative(spacex_api, spacex_query):
    """
    Test verifies attempt to retrieve 
    SpaceX rocket info using invalid query data
    """
    
    spacex_query.rocket_bad(id = SpaceXData.rocket_id)
    response = spacex_api.send_qraphql_query(spacex_query)

    assert response.status_code == HTTPStatus.BAD_REQUEST
    assert (
        response.json()['errors'][0]['extensions']['code'] == SpaceXData.error_text
    )
    