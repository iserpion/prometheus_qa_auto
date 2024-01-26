from modules.ui.page_objects.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
import time
from random import randint


class LoginPage(BasePage):

    # page url
    URL = 'https://www.carid.com/my-account/login/'

    # locators
    NEW_CUSTOMER_BTN = (By.XPATH, '//span[contains(text(), "new customer")]')
    EMAIL_FIELD = (By.ID, 'email')
    PASSWORD_FIELD = (By.ID, 'passwd1')
    SUBMIT_BTN = (By.XPATH, '(//button[@formnovalidate])[2]')


    def __init__(self) -> None:
        super().__init__()
    
    def login(self):
        """Method to login as a new customer to carid.com"""

        # open page
        self.driver.get(LoginPage.URL)

        # select new customer
        try:
            self.element_is_visible(LoginPage.NEW_CUSTOMER_BTN).click()
        except TimeoutException:
            print("Login form is not visible")

        # fill form and submit
        now_date = time.strftime("%Y%m%d%H%M%S", time.localtime())
        email = f'test_user_{now_date}@test.com'
        password = randint(111111, 999999)
        
        try:
            self.element_is_visible(LoginPage.EMAIL_FIELD).send_keys(email)
            self.element_is_visible(LoginPage.PASSWORD_FIELD).send_keys(password)
            self.element_is_visible(LoginPage.SUBMIT_BTN).click()
        except TimeoutException:
            print("Login form fields are not visible")
        
        # wait for login is performed and get current url
        time.sleep(1)
        self.current_url = self.driver.current_url

        return self.current_url
            