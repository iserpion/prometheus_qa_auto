from modules.ui.page_objects.base_page import BasePage
from modules.ui.page_objects.carid_login_page import LoginPage
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from modules.common.generators.address_generator import (
    generated_shipping_address,
    generated_billing_address,
)


class Locators:
    """Class for storing carid.com MyAccount page locators"""

    ACCOUNT_SETTINGS = (By.XPATH, '//div[contains(text(),"Settings")]')
    S_ADDRESS_ADD_NEW_BTN = (By.XPATH, '//button[@data-controller="shipping"]')
    FIRST_NAME = (By.ID, "firstname")
    LAST_NAME = (By.ID, "lastname")
    COMPANY = (By.ID, "company")
    S_ADDRESS = (By.ID, "s_address")
    ADDRESS_2 = (By.ID, "address_2")
    S_CITY = (By.ID, "s_city")
    S_STATE_DROPDOWN = (By.ID, "s_state")
    STATE = (By.XPATH, '//option[@value="AL"]')
    S_ZIPCODE = (By.ID, "s_zipcode")
    PHONE = (By.ID, "phone")
    SUBMIT_BTN = (By.ID, "submitBtn")
    MODAL_BTN = (By.XPATH, '//div[@class="modal-simple"]/button')
    S_ADDRESS_INFO = (By.XPATH, '(//div[@class="ov-hidden"])[1]')
    B_ADDRESS_ADD_NEW_BTN = (By.XPATH, '//button[@data-controller="billing"]')
    B_ADDRESS = (By.ID, "b_address")
    B_CITY = (By.ID, "b_city")
    B_STATE_DROPDOWN = (By.ID, "b_state")
    B_ZIPCODE = (By.ID, "b_zipcode")
    B_ADDRESS_INFO = (By.XPATH, '(//div[@class="ov-hidden"])[3]')
    SUBSCRIBE_BTN = (By.CSS_SELECTOR, 'button.btn.js-subscribe-link')
    ADD_VEHICLE_BTN = (By.CSS_SELECTOR, 'button.simple-btn.-wide.js-mygarage-open-create-popup.mb15')
    YEAR = (By.XPATH, '//div[@data-placeholder="Year"]')
    MAKE = (By.XPATH, '//div[@data-placeholder="Make"]')
    MODEL = (By.XPATH, '//div[@data-placeholder="Model"]')
    GO_BTN = (By.XPATH, '//div[text()="GO"]')
    MMY_OPEN = (By.XPATH, '//div[@class="main-selector -big  -open -with-marker"]')
    MMY_STORED = (By.CSS_SELECTOR, 'a.mygarage-vehicle-title')


class MyAccountPage(BasePage):
    """Class holds attributes and methods of carid.com My Account page"""

    def __init__(self) -> None:
        super().__init__()
        self.ship_address_data = []
        self.ship_address_info = None
        self.bill_address_data = []
        self.bill_address_info = None
        self.is_address_equal = False
        self.vehicle_mmy = None

    def add_shipping_address(self):
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
            shipping_address.phone,
        ]

        # prepare page
        try:
            account_settings = self.element_is_present(Locators.ACCOUNT_SETTINGS)
            self.actions.scroll_to_element(account_settings)
        except TimeoutException:
            print("Account settings element is not present")

        # open shipping address form
        try:
            self.element_is_visible(Locators.S_ADDRESS_ADD_NEW_BTN).click()
        except TimeoutException:
            print("Add new shipping address button is not visible")

        # fill the form
        try:
            self.element_is_visible(Locators.FIRST_NAME).send_keys(
                self.ship_address_data[0]
            )
            self.element_is_visible(Locators.LAST_NAME).send_keys(
                self.ship_address_data[1]
            )
            self.element_is_visible(Locators.COMPANY).send_keys(
                self.ship_address_data[2]
            )
            self.element_is_visible(Locators.S_ADDRESS).send_keys(
                self.ship_address_data[3]
            )
            self.element_is_visible(Locators.ADDRESS_2).send_keys(
                self.ship_address_data[4]
            )
            self.element_is_visible(Locators.S_CITY).send_keys(
                self.ship_address_data[5]
            )
            self.element_is_visible(Locators.S_STATE_DROPDOWN).click()
            self.element_is_visible(Locators.STATE).click()
            self.element_is_visible(Locators.S_ZIPCODE).send_keys(
                self.ship_address_data[8]
            )
            self.element_is_visible(Locators.PHONE).send_keys(self.ship_address_data[9])
        except TimeoutException:
            print("Some of add shipping address form elements are not visible")

        # submit form
        try:
            self.actions.scroll_by_amount(0, 100).perform()
            self.element_is_visible(Locators.SUBMIT_BTN).click()
        except TimeoutException:
            print("Add shipping address submit button is not visible")

        # close modal
        try:
            self.element_is_visible(Locators.MODAL_BTN).click()
        except TimeoutException:
            print("Successfully added shipping address popup OK button is not visible")

        # store shipping address data from My Account page
        try:
            self.ship_address_info = self.element_is_visible(
                Locators.S_ADDRESS_INFO
            ).text
        except TimeoutException:
            print("Shipping address info element is not visible")

        return self.ship_address_info

    def add_billing_address(self):
        """Method adding billing address info on My Account page"""

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
            billing_address.phone,
        ]

        # open billing address form
        try:
            self.element_is_visible(Locators.B_ADDRESS_ADD_NEW_BTN).click()
        except TimeoutException:
            print("Add new billing address button is not visible")

        # fill the form
        try:
            self.element_is_visible(Locators.FIRST_NAME).send_keys(
                self.bill_address_data[0]
            )
            self.element_is_visible(Locators.LAST_NAME).send_keys(
                self.bill_address_data[1]
            )
            self.element_is_visible(Locators.COMPANY).send_keys(
                self.bill_address_data[2]
            )
            self.element_is_visible(Locators.B_ADDRESS).send_keys(
                self.bill_address_data[3]
            )
            self.element_is_visible(Locators.ADDRESS_2).send_keys(
                self.bill_address_data[4]
            )
            self.element_is_visible(Locators.B_CITY).send_keys(
                self.bill_address_data[5]
            )
            self.element_is_visible(Locators.B_STATE_DROPDOWN).click()
            self.element_is_visible(Locators.STATE).click()
            self.element_is_visible(Locators.B_ZIPCODE).send_keys(
                self.bill_address_data[8]
            )
            self.element_is_visible(Locators.PHONE).send_keys(self.bill_address_data[9])
        except TimeoutException:
            print("Some of add billing address form elements are not visible")

        # submit form
        try:
            self.actions.scroll_by_amount(0, 100).perform()
            self.element_is_visible(Locators.SUBMIT_BTN).click()
        except TimeoutException:
            print("Add billing address submit button is not visible")

        # close modal
        try:
            self.element_is_visible(Locators.MODAL_BTN).click()
        except TimeoutException:
            print("Successfully added billing address popup OK button is not visible")

        # store billing address data from My Account page
        try:
            self.bill_address_info = self.element_is_visible(
                Locators.B_ADDRESS_INFO
            ).text
        except TimeoutException:
            print("Billing address info element is not visible")

        return self.bill_address_info

    def validate_address_info(self, address_type):
        """Method for validating shipping/billing address info on My Account page"""

        address_data = []
        address_data_info = ""

        if address_type == "shipping":
            address_data = self.ship_address_data
            address_data_info = self.ship_address_info
        elif address_type == "billing":
            address_data = self.bill_address_data
            address_data_info = self.bill_address_info
        else:
            print("Invalid address_type is given, should be 'shipping' or 'billing'")

        for field in address_data:
            if field in address_data_info:
                self.is_address_equal = True
            else:
                self.is_address_equal = False

        return self.is_address_equal

    def add_vehicle(self):
        """Method for adding vehicle on My Account page"""

        # press add vehicle button
        try:
            self.actions.scroll_to_element(Locators.SUBSCRIBE_BTN)
            self.element_is_visible(Locators.ADD_VEHICLE_BTN).click()
        except TimeoutException:
            print("Add vehicle button is not visible")

        # select make model year
        try:
            year = self.element_is_visible(Locators.YEAR)
            year.click()
            year.send_keys('2006')
            make = self.element_is_visible(Locators.MAKE)
            make.click()
            self.element_is_visible(Locators.MMY_OPEN)
            make.send_keys('toyota')
            model = self.element_is_visible(Locators.MODEL)
            model.click()
            self.element_is_visible(Locators.MMY_OPEN)
            model.send_keys('matrix')
            self.invisibility_of_element_located(Locators.MMY_OPEN, 15)
            self.element_is_visible(Locators.GO_BTN).click()
        except TimeoutException:
            print("Vehicle MMY selectors are not visible")

        # retrieve stored vehicle make model year
        try:
            self.vehicle_mmy = self.element_is_visible(Locators.MMY_STORED).text
        except TimeoutException:
            print("Added vehicle is not visible in Garage")

        return self.vehicle_mmy