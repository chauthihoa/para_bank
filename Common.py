from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.select import Select
from page_element.register import RegisterPageElements
from datetime import datetime

class CommonPage():
    def setUp(self):
        self.drive = self.drive = webdriver.Chrome()

    def open_base_url(self, url='https://parabank.parasoft.com/'):
        self.drive.get(url)

    def find_element(self, ele: str):
        return self.drive.find_element(By.XPATH, ele)

    def find_elements(self, ele: str):
       return self.drive.find_elements(By.XPATH, ele)

    def input_text(self, ele: str, txt: str):
        return self.find_element(ele).send_keys(txt)

    def click_button(self, ele: str):
        return self.find_element(ele).click()
    
    def get_text(self, ele: str):
        return self.find_element(ele).text
    
    def select_option(self, ele: Select, value: str):
        return ele.select_by_visible_text(value)
    
    def tearDown(self):
        self.drive.quit()

    def login(self,username: str, password: str):
     
        self.setUp()
        self.open_base_url()
        self.input_text(RegisterPageElements.TXTBOX_USERNAMELOGIN, username)
        self.input_text(RegisterPageElements.TXTBOX_PASSWORDLOGIN, password)
        self.click_button(RegisterPageElements.BTN_LOGIN)

    def is_date_matching(self,date : str):
        try:
            return bool(datetime.strptime(date,"%m-%d-%Y"))
        except ValueError:
            return False

    def is_value_inrange(self, value : float, fromValue : float, toValue : float):
        return (value >= fromValue and value <= toValue)