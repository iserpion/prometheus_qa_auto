from modules.ui.page_objects.sign_in_page import SignInPage
import pytest


@pytest.mark.ui 
def test_check_incorrect_username_page_object():
    # Create page object
    sign_in_page = SignInPage()

    # Open https://github.com/login page
    sign_in_page.go_to()

    # Attempt to login in GitHub with wrong credentials
    sign_in_page.try_login('page_object@gmail.com', 'wrong password')

    # Check that page title is as expected
    assert sign_in_page.check_title('Sign in to GitHub · GitHub')

    # Close browser
    sign_in_page.close()