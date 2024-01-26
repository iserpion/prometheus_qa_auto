from modules.ui.page_objects.base_page import BasePage
from modules.ui.page_objects.carid_login_page import LoginPage
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from modules.common.generators.address_generator import generated_shipping_address, generated_billing_address


class Locators:
    ACCOUNT_SETTINGS = (By.XPATH, '//div[contains(text(),"Settings")]')
    S_ADDRESS_ADD_NEW_BTN = (By.XPATH, '//button[@data-controller="shipping"]')
    FIRST_NAME = (By.ID, 'firstname')
    LAST_NAME = (By.ID, 'lastname')
    COMPANY = (By.ID, 'company')
    S_ADDRESS = (By.ID, 's_address')
    ADDRESS_2 = (By.ID, 'address_2')
    S_CITY = (By.ID, 's_city')
    S_STATE_DROPDOWN = (By.ID, 's_state')
    STATE = (By.XPATH, '//option[@value="AL"]')
    S_ZIPCODE = (By.ID, 's_zipcode')
    PHONE = (By.ID, 'phone')
    SUBMIT_BTN = (By.ID, 'submitBtn')
    MODAL_BTN = (By.XPATH, '//div[@class="modal-simple"]/button')
    S_ADDRESS_INFO = (By.XPATH, '(//div[@class="ov-hidden"])[1]')
    B_ADDRESS_ADD_NEW_BTN = (By.XPATH, '//button[@data-controller="billing"]')
    B_ADDRESS = (By.ID, 'b_address')
    B_CITY = (By.ID, 'b_city')
    B_STATE_DROPDOWN = (By.ID, 'b_state')
    B_ZIPCODE = (By.ID, 'b_zipcode')
    B_ADDRESS_INFO = (By.XPATH, '(//div[@class="ov-hidden"])[3]')


class MyAccountPage(BasePage):


    def __init__(self) -> None:
        super().__init__()
                

    def  add_shipping_address(self):
        """Method adding shipping address info on My Account page"""

        LoginPage.login(self)

        # generate data for shipping address form
        shipping_address = generated_shipping_address()

        # storing shipping address data
        self.ship_address_data = [
            shipping_address.first_name,
            shipping_address.last_name,
            shipping_address.company,
            shipping_address.address_line_1,
            shipping_address.address_line_2,
            shipping_address.city,
            shipping_address.state,
            shipping_address.country,
            shipping_address.zipcode,
            shipping_address.phone
        ]

        # prepare page
        account_settings = self.element_is_present(Locators.ACCOUNT_SETTINGS)
        self.actions.scroll_to_element(account_settings)

        # open shipping address form
        self.element_is_visible(Locators.S_ADDRESS_ADD_NEW_BTN).click()

        # fill the form
        self.element_is_visible(Locators.FIRST_NAME).send_keys(self.ship_address_data[0])
        self.element_is_visible(Locators.LAST_NAME).send_keys(self.ship_address_data[1])
        self.element_is_visible(Locators.COMPANY).send_keys(self.ship_address_data[2])
        self.element_is_visible(Locators.S_ADDRESS).send_keys(self.ship_address_data[3])
        self.element_is_visible(Locators.ADDRESS_2).send_keys(self.ship_address_data[4])
        self.element_is_visible(Locators.S_CITY).send_keys(self.ship_address_data[5])
        self.element_is_visible(Locators.S_STATE_DROPDOWN).click()
        self.element_is_visible(Locators.STATE).click()
        self.element_is_visible(Locators.S_ZIPCODE).send_keys(self.ship_address_data[8])
        self.element_is_visible(Locators.PHONE).send_keys(self.ship_address_data[9])

        # submit form
        self.actions.scroll_by_amount(0, 100).perform()
        self.element_is_visible(Locators.SUBMIT_BTN).click()

        # close modal
        self.element_is_visible(Locators.MODAL_BTN).click()

        # store shipping address data from My Account page
        self.ship_address_info = self.element_is_visible(Locators.S_ADDRESS_INFO).text

        return self.ship_address_info

  
    def  add_billing_address(self):
        """Method adding shipping address info on My Account page"""

        # LoginPage.login(self)

        # generate data for billing address form
        billing_address = generated_billing_address()

        # storing billing address data
        self.bill_address_data = [
            billing_address.first_name,
            billing_address.last_name,
            billing_address.company,
            billing_address.address_line_1,
            billing_address.address_line_2,
            billing_address.city,
            billing_address.state,
            billing_address.country,
            billing_address.zipcode,
            billing_address.phone
        ]

        # open billing address form
        self.element_is_visible(Locators.B_ADDRESS_ADD_NEW_BTN).click()

        # fill the form
        self.element_is_visible(Locators.FIRST_NAME).send_keys(self.bill_address_data[0])
        self.element_is_visible(Locators.LAST_NAME).send_keys(self.bill_address_data[1])
        self.element_is_visible(Locators.COMPANY).send_keys(self.bill_address_data[2])
        self.element_is_visible(Locators.B_ADDRESS).send_keys(self.bill_address_data[3])
        self.element_is_visible(Locators.ADDRESS_2).send_keys(self.bill_address_data[4])
        self.element_is_visible(Locators.B_CITY).send_keys(self.bill_address_data[5])
        self.element_is_visible(Locators.B_STATE_DROPDOWN).click()
        self.element_is_visible(Locators.STATE).click()
        self.element_is_visible(Locators.B_ZIPCODE).send_keys(self.bill_address_data[8])
        self.element_is_visible(Locators.PHONE).send_keys(self.bill_address_data[9])

        # submit form
        self.actions.scroll_by_amount(0, 100).perform()
        self.element_is_visible(Locators.SUBMIT_BTN).click()

        # close modal
        self.element_is_visible(Locators.MODAL_BTN).click()

        # store billing address data from My Account page
        self.bill_address_info = self.element_is_visible(Locators.B_ADDRESS_INFO).text

        return self.bill_address_info
    
    def validate_address_info(self, address_type):
        """Method for validating shipping/billing address info on My Account page"""

        address_data = []
        address_data_info = ""

        if address_type == 'shipping':
            address_data = self.ship_address_data
            address_data_info = self.ship_address_info
        elif address_type == 'billing':
            address_data = self.bill_address_data
            address_data_info = self.bill_address_info
        else:
            print("Invalid address_type is given, should be 'shipping' or 'billing'")


        self.is_equal = False
        for el in address_data:
            if el in address_data_info:
                self.is_equal = True
            else:
                self.is_equal = False
    
        return self.is_equal
    