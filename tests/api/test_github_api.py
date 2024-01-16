import pytest

@pytest.mark.api
def test_user_exists(github_api):
    user = github_api.get_user('defunkt')
    assert user['login'] == 'defunkt'

@pytest.mark.api
def test_user_not_exists(github_api):
    response = github_api.get_user('butenkosergii')
    assert response['message'] == 'Not Found'

@pytest.mark.api
def test_repo_can_be_found(github_api):
    response = github_api.search_repo('become-qa-auto')
    assert response['total_count'] == 54
    assert 'become-qa-auto' in response['items'][0]['name']

@pytest.mark.api
def test_repo_cannot_be_found(github_api):
    response = github_api.search_repo('funny_repo_non_exist')
    assert response['total_count'] == 0

@pytest.mark.api
def test_repo_with_single_char_be_found(github_api):
    response = github_api.search_repo('s')
    assert response['total_count'] != 0
    
