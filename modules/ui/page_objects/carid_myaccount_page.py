from modules.ui.page_objects.base_page import BasePage
from modules.ui.page_objects.carid_login_page import LoginPage
from modules.ui.page_locators.carid_myaccount_page_locators import (
    CaridMyAccountPageLocators
)
from selenium.common.exceptions import (
    TimeoutException, 
    ElementClickInterceptedException
)
from modules.common.generators.address_generator import (
    generated_shipping_address,
    generated_billing_address,
)


class MyAccountPage(BasePage):
    """Class holds attributes and methods of carid.com My Account page"""

    locators = CaridMyAccountPageLocators()

    def __init__(self) -> None:
        super().__init__()
        self.ship_address_data = []
        self.ship_address_info = None
        self.bill_address_data = []
        self.bill_address_info = None
        self.is_address_equal = False
        self.vehicle_mmy = None

    def add_shipping_address(self):
        """Method for adding shipping address info on My Account page"""

        # login to My account
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

        # scroll to Account Settings section
        account_settings = self.element_is_present(self.locators.ACCOUNT_SETTINGS)
        self.actions.scroll_to_element(account_settings)

        # open shipping address form
        try:
            self.element_is_visible(self.locators.S_ADDRESS_ADD_NEW_BTN).click()
        except (TimeoutException, ElementClickInterceptedException):
            print("Add new shipping address button isn't visible or clickable")

        # fill the form
        self.element_is_visible(self.locators.FIRST_NAME).send_keys(
            self.ship_address_data[0]
        )
        self.element_is_visible(self.locators.LAST_NAME).send_keys(
            self.ship_address_data[1]
        )
        self.element_is_visible(self.locators.COMPANY).send_keys(
            self.ship_address_data[2]
        )
        self.element_is_visible(self.locators.S_ADDRESS).send_keys(
            self.ship_address_data[3]
        )
        self.element_is_visible(self.locators.ADDRESS_2).send_keys(
            self.ship_address_data[4]
        )
        self.element_is_visible(self.locators.S_CITY).send_keys(
            self.ship_address_data[5]
        )
        self.element_is_visible(self.locators.S_STATE_DROPDOWN).click()
        self.element_is_visible(self.locators.STATE).click()
        self.element_is_visible(self.locators.S_ZIPCODE).send_keys(
            self.ship_address_data[8]
        )
        self.element_is_visible(self.locators.PHONE).send_keys(
            self.ship_address_data[9]
        )

        # submit form
        self.actions.scroll_by_amount(0, 100).perform()
        self.element_is_visible(self.locators.SUBMIT_BTN).click()

        # close modal
        self.element_is_visible(self.locators.MODAL_BTN).click()

        # store shipping address data from My Account page
        self.ship_address_info = self.element_is_visible(
            self.locators.S_ADDRESS_INFO
        ).text

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
            self.element_is_visible(self.locators.B_ADDRESS_ADD_NEW_BTN).click()
        except (TimeoutException, ElementClickInterceptedException):
            print("Add new billing address button is not visible or clickable")

        # fill the form
        self.element_is_visible(self.locators.FIRST_NAME).send_keys(
            self.bill_address_data[0]
        )
        self.element_is_visible(self.locators.LAST_NAME).send_keys(
            self.bill_address_data[1]
        )
        self.element_is_visible(self.locators.COMPANY).send_keys(
            self.bill_address_data[2]
        )
        self.element_is_visible(self.locators.B_ADDRESS).send_keys(
            self.bill_address_data[3]
        )
        self.element_is_visible(self.locators.ADDRESS_2).send_keys(
            self.bill_address_data[4]
        )
        self.element_is_visible(self.locators.B_CITY).send_keys(
            self.bill_address_data[5]
        )
        self.element_is_visible(self.locators.B_STATE_DROPDOWN).click()
        self.element_is_visible(self.locators.STATE).click()
        self.element_is_visible(self.locators.B_ZIPCODE).send_keys(
            self.bill_address_data[8]
        )
        self.element_is_visible(self.locators.PHONE).send_keys(
            self.bill_address_data[9]
        )

        # submit form
        self.actions.scroll_by_amount(0, 100).perform()
        self.element_is_visible(self.locators.SUBMIT_BTN).click()

        # close modal
        self.element_is_visible(self.locators.MODAL_BTN).click()

        # store billing address data from My Account page
        self.bill_address_info = self.element_is_visible(
            self.locators.B_ADDRESS_INFO
        ).text

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
            self.actions.scroll_to_element(self.locators.SUBSCRIBE_BTN)
            self.element_is_visible(self.locators.ADD_VEHICLE_BTN).click()
        except (TimeoutException, ElementClickInterceptedException):
            print("Add vehicle button is not visible or clickable")

        # select make model year
        year = self.element_is_visible(self.locators.YEAR)
        year.click()
        year.send_keys('2006')
        make = self.element_is_visible(self.locators.MAKE)
        make.click()
        self.element_is_visible(self.locators.MMY_OPEN)
        make.send_keys('toyota')
        model = self.element_is_visible(self.locators.MODEL)
        model.click()
        self.element_is_visible(self.locators.MMY_OPEN)
        model.send_keys('matrix')

        # save selected vehicle make model year
        try:
            go_btn = self.element_is_clickable(self.locators.GO_BTN)
            go_btn.click()
            self.page_execute_script('click', go_btn)
        except (TimeoutException, ElementClickInterceptedException):
            print("GO button is not visible or clickable")

        # retrieve stored vehicle make model year
        self.vehicle_mmy = self.element_is_visible(self.locators.MMY_STORED).text

        return self.vehicle_mmy
    