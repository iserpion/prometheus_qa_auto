from modules.ui.page_objects.base_page import BasePage
from modules.ui.page_locators.allo_main_page_locators import (
    AlloMainPageLocators
)
from selenium.common.exceptions import (
    TimeoutException,
    ElementClickInterceptedException,
)


class MainPage(BasePage):
    """Class holds attributes and methods of allo.ua main page"""

    URL = "https://allo.ua/"
    locators = AlloMainPageLocators()

    def __init__(self) -> None:
        super().__init__()
        self.product_data = {}
        self.cart_data = {}
        self.empty_cart_msg = ""
        self.increase_data = {}
        self.decrease_data = {}
        self.current_url = ""

    def go_to(self):
        """Method to open allo.ua main page"""

        self.driver.get(MainPage.URL)

    def add_random_top_product_to_cart(self):
        """Method for adding random top product to cart from allo.ua main page"""

        # maximize browser window
        self.driver.maximize_window()

        # scroll to top products section
        self.page_execute_script("scroll", 800)

        # close promo popup if displayed
        try:
            self.element_is_visible(self.locators.PRE_ORDER_CLOSE_BTN).click()
        except TimeoutException:
            print("Promo popup element is not visible")

        # save main page product data
        self.product_data = {
            "product_title": self.element_is_visible(
                self.locators.TOP_PRODUCT_TITLE
            ).text,
            "product_price": self.element_is_visible(
                self.locators.TOP_PRODUCT_PRICE
            ).text,
        }

        # add product to cart
        try:
            self.element_is_visible(self.locators.TOP_PRODUCT_BUY_BTN).click()
        except TimeoutException:
            print("Unable to locate product buy button")

        # save data from cart popup
        self.cart_data = {
            "popup_title": self.element_is_visible(
                self.locators.CART_POPUP_TITLE
            ).text,
            "product_title": self.element_is_visible(
                self.locators.CART_PRODUCT_TITLE
            ).text,
            "product_price": self.element_is_visible(
                self.locators.CART_PRODUCT_PRICE
            ).text,
            "total_price": self.element_is_visible(
                self.locators.CART_TOTAL_PRICE
            ).text,
        }
       
        return self.product_data, self.cart_data

    @staticmethod
    def get_nums_from_str(string):
        """
        Method for getting numbers from string.
        It is needed as prices strings on allo.ua 
        can contain spaces and special characters
        """

        return int("".join(char for char in string if char.isdigit()))

    def remove_product_from_cart(self):
        """Method for removing product from cart popup"""

        # remove product from cart
        try:
            self.element_is_visible(self.locators.CART_REMOVE_BTN).click()
        except (TimeoutException, ElementClickInterceptedException):
            print("Product remove button is not visible or clickable")

        # save empty cart message
        self.empty_cart_msg = self.element_is_visible(
            self.locators.CART_EMPTY_MSG
        ).text

        return self.empty_cart_msg

    def increase_product_qty_in_cart(self):
        """Method for increasing quantity of product in cart"""

        # increase product quantity twice
        try:
            self.element_is_visible(self.locators.CART_QTY_PLUS).click()
            self.element_is_visible(self.locators.CART_QTY_PLUS).click()
        except (TimeoutException, ElementClickInterceptedException):
            print("Increase qty button is not visible or clickable")

        # wait until cart updating if finished
        self.invisibility_of_element_located(self.locators.CART_POPUP_LOADING)

        # save data after increasing
        self.increase_data = {
            "product_price": self.get_nums_from_str(
                self.product_data["product_price"]
            ),
            "cart_price": self.get_nums_from_str(
                self.element_is_visible(self.locators.CART_PRODUCT_PRICE).text
            ),
            "total_price": self.get_nums_from_str(
                self.element_is_visible(self.locators.CART_TOTAL_PRICE).text
            ),
        }

    def decrease_product_qty_in_cart(self):
        """Method for decreasing quantity of product in cart"""

        # decrease product quantity
        try:
            self.element_is_visible(self.locators.CART_QTY_MINUS).click()
        except (TimeoutException, ElementClickInterceptedException):
            print("Decrease qty button is not visible or clickable")

        # wait until cart updating if finished
        self.invisibility_of_element_located(self.locators.CART_POPUP_LOADING)

        # save data after decreasing
        self.decrease_data = {
            "product_price": self.get_nums_from_str(
                self.product_data["product_price"]
            ),
            "cart_price": self.get_nums_from_str(
                self.element_is_visible(self.locators.CART_PRODUCT_PRICE).text
            ),
            "total_price": self.get_nums_from_str(
                self.element_is_visible(self.locators.CART_TOTAL_PRICE).text
            ),
        }

    def validate_increase(self):
        """Method for validating that product quantity is increased"""

        # retrieving and store price data after increasing
        product_price_in = self.increase_data["product_price"]
        cart_price_in = self.increase_data["cart_price"]
        total_price_in = self.increase_data["total_price"]

        return (
            cart_price_in == product_price_in * 3
            and total_price_in == cart_price_in
        )  # after increasing qty = 3
  
    def validate_decrease(self):
        """Method for validating that product quantity is decreased"""

        # retrieving and store price data after decreasing
        product_price_de = self.decrease_data["product_price"]
        cart_price_de = self.decrease_data["cart_price"]
        total_price_de = self.decrease_data["total_price"]

        return (
            cart_price_de == product_price_de * 2
            and total_price_de == cart_price_de
        )  # after decreasing qty = 2

    def proceed_to_checkout(self):
        """Method for transition from cart popup to checkout page"""

        try:
            self.element_is_visible(self.locators.CHECKOUT_BTN).click()
        except (TimeoutException, ElementClickInterceptedException):
            print("Proceed to checkout button is not visible or clickable")

        # wait until page transition is performed and get current url
        self.title_is_updated("Оформлення замовлення – інтернет-магазин ALLO.ua!")
        self.current_url = self.driver.current_url

        return self.current_url
