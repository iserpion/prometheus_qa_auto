from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait as Wait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains

class BasePage:

    def __init__(self) -> None:
        
        _options = Options()
        
        # Add option to disable Chrome allow notifications prompt
        # Add option to disable Chrome autofill e.g. save address prompt
        _prefs = {
            "profile.default_content_setting_values.notifications": 2,
            "autofill.profile_enabled": False
            }
        
        _options.add_experimental_option("prefs", _prefs)

        # Add option to not automatically close browser
        _options.add_experimental_option("detach", True)

        # driver
        self.driver = webdriver.Chrome(options = _options)

        # actions
        self.actions = ActionChains(self.driver)


    def element_is_visible(self, locator, timeout=15):
        """Method for waiting until element is visible. Returns element object"""
        
        return Wait(self.driver, timeout).until(EC.visibility_of_element_located(locator))
    
    def element_is_present(self, locator, timeout=10):
        """Method for waiting until element is visible. Returns element object"""
        
        return Wait(self.driver, timeout).until(EC.presence_of_element_located(locator))

    def page_execute_script(self, type, value):
        """Method for executing JS scripts on page"""

        if type == 'click':
            return self.driver.execute_script("arguments[0].click();", value)
        elif type == 'scroll':
            return self.driver.execute_script(f"window.scrollTo(0, {value})")
        else:
            print("Wrong arguments: type['click', 'scroll'] | value[element, pixels]")

    
    def close(self):
        self.driver.close()
