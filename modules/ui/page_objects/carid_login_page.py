from modules.ui.page_objects.base_page import BasePage
from selenium.webdriver.common.by import By
import time
from random import randint


class LoginPage(BasePage):
    """Class holds elements and methods of carid.com login page"""

    # page url
    URL = "https://www.carid.com/my-account/login/"

    # page locators
    NEW_CUSTOMER_BTN = (By.XPATH, '//span[contains(text(), "new customer")]')
    EMAIL_FIELD = (By.ID, "email")
    PASSWORD_FIELD = (By.ID, "passwd1")
    SUBMIT_BTN = (By.XPATH, "(//button[@formnovalidate])[2]")

    def __init__(self) -> None:
        super().__init__()
        self.current_url = None

    def login(self):
        """Method to login as a new customer to carid.com"""

        # open carid.com login page
        self.driver.get(LoginPage.URL)

        # select new customer option
        self.element_is_visible(LoginPage.NEW_CUSTOMER_BTN).click()

        # prepare data for login as a new customer
        now_date = time.strftime("%Y%m%d%H%M%S", time.localtime())
        email = f"test_user_{now_date}@test.com"
        password = randint(111111, 999999)

        # fill form and submit
        self.element_is_visible(LoginPage.EMAIL_FIELD).send_keys(email)
        self.element_is_visible(LoginPage.PASSWORD_FIELD).send_keys(password)
        self.element_is_visible(LoginPage.SUBMIT_BTN).click()

        # wait until login is performed and get current url
        self.title_is_updated("CARiD.com - My Account")
        self.current_url = self.driver.current_url

        return self.current_url
