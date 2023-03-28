from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.select import Select
from page_element.register import RegisterPageElements
import unittest

class CommonPage():
    def setUp(self):
        self.drive = self.drive = webdriver.Chrome()

    def open_base_url(self, url='https://parabank.parasoft.com/'):
        self.drive.get(url)

    def find_element(self, ele: str):
        return self.drive.find_element(By.XPATH, ele)

    def find_elements(self, ele: str):
       return self.drive.find_elements(By.XPATH, ele)

    def input_text(self, ele: WebElement, txt: str):
        return ele.send_keys(txt)

    def click_button(self, ele: WebElement):
        return ele.click()
    
    def get_text(self, ele: WebElement):
        return ele.text
    
    def select_option(self, ele: Select, value: str):
        return ele.select_by_visible_text(value)
    
    def tearDown(self):
        self.drive.quit()

    def login(self,username: str, password: str):
     
        self.setUp()
        self.open_base_url()
        txt_usernamelogin = self.find_element(
                RegisterPageElements.TXTBOX_USERNAMELOGIN)
        self.input_text(txt_usernamelogin, username)
        txt_passwordlogin = self.find_element(
                RegisterPageElements.TXTBOX_PASSWORDLOGIN)
        self.input_text(txt_passwordlogin, password)
        btn_login = self.find_element(RegisterPageElements.BTN_LOGIN)
        self.click_button(btn_login)

    # def loginAfterLogout(self,username: str, password: str):
    #     initial = InitialPage()
    #     txt_usernamelogin = initial.find_element(self,
    #             RegisterPageElements.TXTBOX_USERNAMELOGIN)
    #     initial.input_text(self,txt_usernamelogin, username)
    #     txt_passwordlogin = initial.find_element(self,
    #             RegisterPageElements.TXTBOX_PASSWORDLOGIN)
    #     initial.input_text(self,txt_passwordlogin, password)
    #     btn_login = initial.find_element(RegisterPageElements.BTN_LOGIN)
    #     initial.click_button(self,btn_login)