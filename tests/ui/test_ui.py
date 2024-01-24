import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

@pytest.mark.ui
def test_check_incorrect_username():
    # Creation an object for controlling browser
    driver = webdriver.Chrome()

    # Open https://github.com/login page
    driver.get('https://github.com/login')

    # Find field for entering username or email
    login_elem = driver.find_element(By.ID, 'login_field')

    # Enter wrong email
    login_elem.send_keys('wrong@email.com') 
    
    # Find filed for entering password
    pass_elem = driver.find_element(By.ID, 'password')

    # Enter wrong password
    pass_elem.send_keys('wrong_password')

    # Find sign in button
    btn_elem = driver.find_element(By.NAME, 'commit')

    # Emulation of click by mouse left button
    btn_elem.click()
    
    # Check that page title is correct
    assert driver.title == 'Sign in to GitHub · GitHub'

    # Close browser
    driver.close()