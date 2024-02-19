from selenium.webdriver.common.by import By


class NovaDeliveryPageLocators:
    """Class holds novaposhta.ua delivery page locators"""

    ORIGIN_CITY_DROPDOWN = (By.ID, 'DeliveryForm_senderCity')
    ORIGIN_KYIV = (By.XPATH, '//div[@class="jspPane"]/descendant::span[4]')
    DEST_CITY_DROPDOWN = (By.ID, 'DeliveryForm_recipientCity')
    DEST_ODESA = (By.XPATH, '//div[@class="jspPane"]/descendant::span[8]')
    ANNOUNCED_PRICE = (By.NAME, "DeliveryForm[optionsSeat][1][cost]")
    WEIGHT = (By.NAME, "DeliveryForm[optionsSeat][1][weight]")
    LENGTH = (By.NAME, "DeliveryForm[optionsSeat][1][volumetricLength]")
    WIDTH = (By.NAME, "DeliveryForm[optionsSeat][1][volumetricWidth]")
    HEIGHT = (By.NAME, "DeliveryForm[optionsSeat][1][volumetricHeight]")
    PACKING_CHECKBOX = (By.ID, "add-pack")
    PACKING_DROPDOWN = (By.NAME, "DeliveryForm[packing][1][packType]")
    PACKING_10KG_BOX = (By.XPATH, '//span[contains(text(),"Коробка (10 кг)")]')
    FLOOR_COUNT = (By.NAME, "DeliveryForm[floorCountAsc]")
    ELEVATOR_CHECKBOX = (By.ID, "DeliveryForm_elevatorAsc")
    BACK_DELIVERY_CHECKBOX = (By.ID, "DeliveryForm_backDelivery")
    BACK_DELIVERY_TYPE_DROPDOWN = (
        By.XPATH,
        '//span[contains(text(), "Виберіть значення")]',
    )
    BACK_DELIVERY_MONEY_OPTION = (By.XPATH, '//li[@data-value="Money"]')
    MONEY_AMOUNT = (By.ID, "DeliveryForm_backDelivery_amount")
    CALCULATE_COST_BTN = (By.NAME, "yt0")
    CALCULATED_COST_TEXT = (By.XPATH, '//td[@colspan="2"]')
    CLOSE_POPUP_BTN = (By.XPATH, '(//i[@class="click close btn_x"])[2]')
