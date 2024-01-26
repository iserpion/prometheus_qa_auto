from modules.ui.page_objects.base_page import BasePage
from selenium.webdriver.common.by import By
import time

class Locators:
    """Class for storing novaposhta.ua delivery page locators"""

    ORIGIN_CITY_DROPDOWN = (By.XPATH, '//div[@class="b_autocomplete s_activated"]/ins')
    ORIGIN_KYIV = (By.XPATH, '//div[@class="jspPane"]/descendant::span[4]')
    DEST_CITY_DROPDOWN = (By.XPATH, '(//div[@class="b_autocomplete s_activated"])[2]//ins')
    DEST_ODESA = (By.XPATH, '//div[@class="jspPane"]/descendant::span[8]')
    ANNOUNCED_PRICE = (By.NAME,'DeliveryForm[optionsSeat][1][cost]')
    WEIGHT = (By.NAME,'DeliveryForm[optionsSeat][1][weight]')
    LENGTH = (By.NAME,'DeliveryForm[optionsSeat][1][volumetricLength]')
    WIDTH = (By.NAME,'DeliveryForm[optionsSeat][1][volumetricWidth]')
    HEIGHT = (By.NAME,'DeliveryForm[optionsSeat][1][volumetricHeight]')
    PACKING_CHECKBOX = (By.ID,'add-pack')
    PACKING_DROPDOWN = (By.NAME,'DeliveryForm[packing][1][packType]')
    PACKING_10KG_BOX = (By.XPATH, '//span[contains(text(),"Коробка (10 кг)")]')
    FLOOR_COUNT = (By.NAME,'DeliveryForm[floorCountAsc]')
    ELEVATOR_CHECKBOX = (By.ID,'DeliveryForm_elevatorAsc')
    BACK_DELIVERY_CHECKBOX = (By.ID,'DeliveryForm_backDelivery')
    BACK_DELIVERY_TYPE_DROPDOWN = (By.XPATH, '//span[contains(text(), "Виберіть значення")]')
    BACK_DELIVERY_MONEY_OPTION = (By.XPATH, '//li[@data-value="Money"]')
    MONEY_AMOUNT = (By.ID,'DeliveryForm_backDelivery_amount')
    CALCULATE_DELIVERY_BTN = (By.NAME, 'yt0')
    CALCULATED_COST_TEXT = (By.XPATH, '//td[@colspan="2"]')

class DeliveryPage(BasePage):

    URL = 'https://novaposhta.ua/delivery'

    def __init__(self) -> None:
        super().__init__()
    
    def go_to(self):
        self.driver.get(DeliveryPage.URL)

    def fill_fields(self):
        """Method for filling delivery page fields and submit"""

        # select origin city
        self.element_is_visible(Locators.ORIGIN_CITY_DROPDOWN).click()
        self.element_is_visible(Locators.ORIGIN_KYIV).click()

        # select destination city
        self.element_is_visible(Locators.DEST_CITY_DROPDOWN).click()
        self.element_is_visible(Locators.DEST_ODESA).click()

        # enter package info
        self.element_is_visible(Locators.ANNOUNCED_PRICE).send_keys('200')
        self.element_is_visible(Locators.WEIGHT).send_keys('10')
        self.element_is_visible(Locators.LENGTH).send_keys('50')
        self.element_is_visible(Locators.WIDTH).send_keys('40')
        self.element_is_visible(Locators.HEIGHT).send_keys('20')

        # add packing option
        packing_checkbox = self.element_is_visible(Locators.PACKING_CHECKBOX)
        self.page_execute_script('click', packing_checkbox)

        # select packing option
        self.element_is_visible(Locators.PACKING_DROPDOWN).click()
        packing_10kg_box = self.element_is_present(Locators.PACKING_10KG_BOX)
        self.actions.scroll_to_element(packing_10kg_box).perform()
        packing_10kg_box.click()
        self.actions.scroll_by_amount(0, 100).perform()

        # add elevate option
        self.element_is_visible(Locators.FLOOR_COUNT).send_keys('7')
        self.element_is_visible(Locators.ELEVATOR_CHECKBOX).click()

        # add back delivery option
        self.element_is_visible(Locators.BACK_DELIVERY_CHECKBOX).click()

        # select type of back delivery
        self.element_is_visible(Locators.BACK_DELIVERY_TYPE_DROPDOWN).click()
        money_option = self.element_is_visible(Locators.BACK_DELIVERY_MONEY_OPTION)
        self.page_execute_script('click', money_option)

        # enter back delivery amount of money
        self.element_is_visible(Locators.MONEY_AMOUNT).send_keys('1000')
    
    def calculate_delivery(self):
        """Method for delivery calculate action on Delivery page"""

        # press calculate cost button
        self.element_is_visible(Locators.CALCULATE_DELIVERY_BTN).click()

        # wait until calculation is done
        time.sleep(3)

        # save cost string to variable
        calculated_cost_element = self.element_is_visible(Locators.CALCULATED_COST_TEXT)
        self.calculated_cost = calculated_cost_element.text

        return self.calculated_cost
