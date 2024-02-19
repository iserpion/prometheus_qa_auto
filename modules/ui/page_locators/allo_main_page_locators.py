from selenium.webdriver.common.by import By
from random import randint


class AlloMainPageLocators:
    """Class holds allo.ua main page locators"""

    PRE_ORDER_CLOSE_BTN = (By.XPATH, '//button[@aria-label="Close"]')

    # Top product current price locator can vary so such huge xpath is used
    top10 = randint(1, 10)
    buy_btn_x = f'//div[@data-products-type="top"]/descendant::button[@class="v-btn--cart"][{top10}]'

    TOP_PRODUCT_BUY_BTN = (By.XPATH, buy_btn_x)
    TOP_PRODUCT_TITLE = (
        By.XPATH,
        f'{buy_btn_x}/preceding::a[@class="product-card__title h-pc__title"][1]',
    )
    TOP_PRODUCT_PRICE = (By.XPATH, f'{buy_btn_x}/preceding::span[@class="sum"][1]')
    CART_POPUP_TITLE = (By.XPATH, '//span[@class="v-modal__cmp-header-title"]')
    CART_PRODUCT_PRICE = (By.XPATH, '//div[@class="price-box__cur"]')
    CART_PRODUCT_TITLE = (By.XPATH, "//span[@data-product-name]")
    CART_TOTAL_PRICE = (By.XPATH, "//span[@data-order-total]")
    CART_QTY_PLUS = (By.CSS_SELECTOR, "svg.vi__plus")
    CART_QTY_MINUS = (By.CSS_SELECTOR, "svg.vi__minus")
    CART_REMOVE_BTN = (By.CSS_SELECTOR, "svg.remove")
    CART_EMPTY_MSG = (By.CSS_SELECTOR, "div.cart-popup_empty>p")
    CART_POPUP_LOADING = (By.CSS_SELECTOR, "div.cart-popup__content.loading")
    CHECKOUT_BTN = (By.CSS_SELECTOR, 'button.order-now')
    