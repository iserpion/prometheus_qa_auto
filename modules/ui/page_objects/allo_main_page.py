from modules.ui.page_objects.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from random import randint
import time


class Locators:
    """Class for storing allo.ua main page locators"""

    PRE_ORDER_CLOSE_BTN = (By.XPATH, '//button[@aria-label="Close"]')

    # Top product current price locator can vary so such huge xpath is used
    top10 = randint(1, 10)
    buy_btn_x = f'//div[@data-products-type="top"]/descendant::button[@class="v-btn--cart"][{top10}]'

    TOP_PRODUCT_BUY_BTN = (By.XPATH, buy_btn_x)
    TOP_PRODUCT_TITLE = (By.XPATH, f'{buy_btn_x}/preceding::a[@class="product-card__title h-pc__title"][1]')
    TOP_PRODUCT_PRICE = (By.XPATH, f'{buy_btn_x}/preceding::span[@class="sum"][1]')
    CART_POPUP_TITLE = (By.XPATH, '//span[@class="v-modal__cmp-header-title"]')
    CART_PRODUCT_PRICE = (By.XPATH, '//div[@class="price-box__cur"]')
    CART_PRODUCT_TITLE = (By.XPATH, "//span[@data-product-name]")
    CART_TOTAL_PRICE = (By.XPATH, "//span[@data-order-total]")
    CART_QTY_PLUS = (By.CSS_SELECTOR, "svg.vi__plus")
    CART_QTY_MINUS = (By.CSS_SELECTOR, "svg.vi__minus")
    CART_REMOVE_BTN = (By.CSS_SELECTOR, "svg.remove")
    CART_EMPTY_MSG = (By.CSS_SELECTOR, "div.cart-popup_empty>p")
    CART_POPUP = (By.CSS_SELECTOR, "div.cart-popup")


class MainPage(BasePage):
    URL = "https://allo.ua/"

    def __init__(self) -> None:
        super().__init__()

    def go_to(self):
        self.driver.get(MainPage.URL)

    def add_product_to_cart(self):
        """Method for adding top product to cart from allo.ua main page"""

        # maximize browser window
        self.driver.maximize_window()

        # scroll to top products section
        self.page_execute_script('scroll', 800)

        # close pre-order popup
        try:
            self.element_is_visible(Locators.PRE_ORDER_CLOSE_BTN).click()
        except TimeoutException:
            print("Pre-order popup element is not visible")

        # save product data on main page
        try:
            self.product_data = {
            "product_title" : self.element_is_visible(Locators.TOP_PRODUCT_TITLE).text,
            "product_price" : self.element_is_visible(Locators.TOP_PRODUCT_PRICE).text,
            }
        except TimeoutException:
            print("Unable to locate element on main page")

        # add product to cart
        try:
            self.element_is_visible(Locators.TOP_PRODUCT_BUY_BTN).click()
        except TimeoutException:
            print("Unable to locate product button")

        # save data from cart popup
        try:
            self.cart_data = {
            "popup_title" : self.element_is_visible(Locators.CART_POPUP_TITLE).text,
            "product_title" : self.element_is_visible(Locators.CART_PRODUCT_TITLE).text,
            "product_price" : self.element_is_visible(Locators.CART_PRODUCT_PRICE).text,
            "total_price" : self.element_is_visible(Locators.CART_TOTAL_PRICE).text,
            }
        except TimeoutException:
            print("Unable to locate element in cart popup")

        return self.product_data, self.cart_data

    def get_nums_from_str(self, string):
        """Method for getting numbers from string.
        It is needed as prices strings on allo.ua can contain spaces and special characters"""

        return int("".join(char for char in string if char.isdigit()))

    def remove_product_from_cart(self):
        """Method for removing product from cart popup"""

        # remove product from cart
        self.element_is_visible(Locators.CART_REMOVE_BTN).click()

        # save empty cart message
        self.empty_cart_msg = self.element_is_visible(Locators.CART_EMPTY_MSG).text

        return self.empty_cart_msg
    
    def increase_product_qty_in_cart(self):
        """Method for increasing quantity of product in cart"""

        # increase product quantity
        self.element_is_visible(Locators.CART_QTY_PLUS).click()
        self.element_is_visible(Locators.CART_QTY_PLUS).click()
        
        # add explicit wait as after increasing need some time to price locators are updated 
        time.sleep(1)

        # save data after increasing
        self.increase_data = {
            "product_price" : self.get_nums_from_str(self.product_data['product_price']),
            "cart_price" : self.get_nums_from_str(self.element_is_visible(Locators.CART_PRODUCT_PRICE).text),
            "total_price" : self.get_nums_from_str(self.element_is_visible(Locators.CART_TOTAL_PRICE).text), 
        }
    
    def decrease_product_qty_in_cart(self):
        """Method for decreasing quantity of product in cart"""

        # decrease product quantity
        self.element_is_visible(Locators.CART_QTY_MINUS).click()
        
        # add explicit wait as after decreasing need some time to price locators are updated 
        time.sleep(1)
        
        # save data after decreasing
        self.decrease_data = {
            "product_price" : self.get_nums_from_str(self.product_data['product_price']),
            "cart_price" : self.get_nums_from_str(self.element_is_visible(Locators.CART_PRODUCT_PRICE).text),
            "total_price" : self.get_nums_from_str(self.element_is_visible(Locators.CART_TOTAL_PRICE).text), 
        }


    def validate_increase_decrease(self, operation):
        """Method for validating that product quantity is increased/decreased"""

        if operation == 'increase':
            # retrieving and store price data after increasing
            product_price_in = self.increase_data['product_price']
            cart_price_in = self.increase_data['cart_price']
            total_price_in = self.increase_data['total_price']

            return cart_price_in == product_price_in * 3 and total_price_in == cart_price_in  # after increasing qty = 3
        
        elif operation == 'decrease':
            # retrieving and store price data after decreasing
            product_price_de = self.decrease_data['product_price']
            cart_price_de = self.decrease_data['cart_price']
            total_price_de = self.decrease_data['total_price']

            return cart_price_de == product_price_de * 2 and total_price_de == cart_price_de  # after decreasing qty = 2
        
        else:
            result = "Invalid operation is given, use 'increase' or 'decrease'"
            print(result)
