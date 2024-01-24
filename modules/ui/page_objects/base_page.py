from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait as Wait
from selenium.webdriver.support import expected_conditions as EC

class BasePage:

    def __init__(self) -> None:
        
        _options = Options()

        # Add option to dismiss Chrome notifications "alert"
        _prefs = {"profile.default_content_setting_values.notifications": 2}
        _options.add_experimental_option("prefs", _prefs)

        # Add option to not automatically close browser
        _options.add_experimental_option("detach", True)
        
        # driver
        self.driver = webdriver.Chrome(options = _options)

    def element_is_visible(self, locator, timeout=15):
        return Wait(self.driver, timeout).until(EC.visibility_of_element_located(locator))
    
    def close(self):
        self.driver.close()