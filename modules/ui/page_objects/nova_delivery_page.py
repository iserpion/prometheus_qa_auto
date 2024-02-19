from modules.ui.page_objects.base_page import BasePage
from modules.ui.page_locators.nova_delivery_page_locators import (
    NovaDeliveryPageLocators
)
from selenium.common.exceptions import (
    TimeoutException,
    ElementClickInterceptedException,
)


class DeliveryPage(BasePage):
    """Class holds attributes and methods of novaposhta.ua delivery page"""

    URL = "https://novaposhta.ua/delivery"
    locators = NovaDeliveryPageLocators()

    def __init__(self) -> None:
        super().__init__()
        self.calculated_cost = ""

    def go_to(self):
        """Method for opening delivery novaposhta.ua page"""

        self.driver.get(DeliveryPage.URL)

    def fill_form_fields(self):
        """Method for filling delivery page fields"""

        # prepare page - close promo popup if displayed
        try:
            self.element_is_visible(self.locators.CLOSE_POPUP_BTN).click()
        except (TimeoutException, ElementClickInterceptedException):
            print("Close popup button is not visible or clickable")

        # select origin city
        self.element_is_visible(self.locators.ORIGIN_CITY_DROPDOWN).click()
        self.element_is_visible(self.locators.ORIGIN_KYIV).click()

        # select destination city
        self.element_is_visible(self.locators.DEST_CITY_DROPDOWN).click()
        self.element_is_visible(self.locators.DEST_ODESA).click()

        # enter package info
        self.element_is_visible(self.locators.ANNOUNCED_PRICE).send_keys("200")
        self.element_is_visible(self.locators.WEIGHT).send_keys("10")
        self.element_is_visible(self.locators.LENGTH).send_keys("50")
        self.element_is_visible(self.locators.WIDTH).send_keys("40")
        self.element_is_visible(self.locators.HEIGHT).send_keys("20")

        # add packing option
        pack_checkbox = self.element_is_visible(self.locators.PACKING_CHECKBOX)
        self.page_execute_script("click", pack_checkbox)

        # select packing option
        self.element_is_visible(self.locators.PACKING_DROPDOWN).click()
        pack_10kg_box = self.element_is_present(self.locators.PACKING_10KG_BOX)
        self.actions.scroll_to_element(pack_10kg_box).perform()
        pack_10kg_box.click()
        self.actions.scroll_by_amount(0, 100).perform()

        # add elevate option
        self.element_is_visible(self.locators.FLOOR_COUNT).send_keys("7")
        self.element_is_visible(self.locators.ELEVATOR_CHECKBOX).click()

        # add back delivery option
        self.element_is_visible(self.locators.BACK_DELIVERY_CHECKBOX).click()

        # select type of back delivery
        self.element_is_visible(
            self.locators.BACK_DELIVERY_TYPE_DROPDOWN
        ).click()
        money_option = self.element_is_visible(
            self.locators.BACK_DELIVERY_MONEY_OPTION
        )
        self.page_execute_script("click", money_option)

        # enter back delivery amount of money
        self.element_is_visible(self.locators.MONEY_AMOUNT).send_keys("1000")

    def calculate_delivery(self):
        """Method for delivery calculate action on Delivery page"""

        # press calculate cost button
        try:
            self.element_is_visible(self.locators.CALCULATE_COST_BTN).click()
        except (TimeoutException, ElementClickInterceptedException):
            print("Calculate cost button is not visible or clickable")

        # save cost string to variable
        calculated_cost_element = self.element_is_visible(
            self.locators.CALCULATED_COST_TEXT
        )
        self.calculated_cost = calculated_cost_element.text

        return self.calculated_cost
