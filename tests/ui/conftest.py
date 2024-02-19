import pytest
from modules.ui.page_objects.github_sign_in_page import SignInPage
from modules.ui.page_objects.allo_main_page import MainPage
from modules.ui.page_objects.nova_delivery_page import DeliveryPage
from modules.ui.page_objects.carid_login_page import LoginPage
from modules.ui.page_objects.carid_myaccount_page import MyAccountPage


@pytest.fixture
def github_page():
    page = SignInPage()

    yield page

    page.close()


@pytest.fixture
def allo_page():
    page = MainPage()
    page.go_to()

    yield page

    page.close()


@pytest.fixture
def nova_page():
    page = DeliveryPage()
    page.go_to()

    yield page

    page.close()


@pytest.fixture(scope='module')
def carid_page(request):
    param = request.param

    if param == 'login':
        page = LoginPage()
    elif param == 'my_account':
        page = MyAccountPage()

    yield page

    page.close()
    