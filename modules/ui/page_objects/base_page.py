from selenium import webdriver


class BasePage:

    def __init__(self) -> None:
        self.driver = webdriver.Chrome()
    
    def close(self):
        self.driver.close()