import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from page_element.Forgot_Info import ForgotInfoElements
import json

class ForgotInfoPage(unittest.TestCase):
    # Pre-condition: Information into account_data.json should be registered successfully by running Register_Test.py
    f = open('./data/account_data.json')
    acc_data = json.load(f)
    f.close()
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

    def test_forgot_successfully(self):
        self.open_base_url()
        link_forgotinfo = self.find_element(ForgotInfoElements.LINK_FORGOTINFO)
        self.click_button(link_forgotinfo)
        txt_firstname = self.find_element(ForgotInfoElements.TXTBOX_FIRSTNAME)
        self.input_text(txt_firstname, self.acc_data["First Name"])
        txt_lastname = self.find_element(ForgotInfoElements.TXTBOX_LASTNAME)
        self.input_text(txt_lastname, self.acc_data["Last Name"])
        txt_street = self.find_element(ForgotInfoElements.TXTBOX_STREET)
        self.input_text(txt_street, self.acc_data["Street"])
        txt_city = self.find_element(ForgotInfoElements.TXTBOX_CITY)
        self.input_text(txt_city, self.acc_data["City"])
        txt_state = self.find_element(ForgotInfoElements.TXTBOX_STATE)
        self.input_text(txt_state, self.acc_data["State"])
        txt_zipcode = self.find_element(ForgotInfoElements.TXTBOX_ZIPCODE)
        self.input_text(txt_zipcode, self.acc_data["Zipcode"])
        txt_ssn = self.find_element(ForgotInfoElements.TXTBOX_SSN)
        self.input_text(txt_ssn, self.acc_data["SSN"])
        btn_findinfo = self.find_element(ForgotInfoElements.BTN_FINDINFO)
        self.click_button(btn_findinfo)
        except_result = "Username: " + self.acc_data["Username"] + '\n' + "Password: " + self.acc_data["Password"]
        actual_result = self.find_elements(ForgotInfoElements.TXT_USERNAMEPW)

    def test_validation(self):
        self.open_base_url()
        link_forgotinfo = self.find_element(ForgotInfoElements.LINK_FORGOTINFO)
        self.click_button(link_forgotinfo)
        btn_findinfo = self.find_element(ForgotInfoElements.BTN_FINDINFO)
        self.click_button(btn_findinfo)
        txt_firstname_error = self.find_element(ForgotInfoElements.TXT_FIRSTNAME_ERROR)
        self.assertEqual(self.get_text(txt_firstname_error),'First name is required.')
        txt_lastname_error = self.find_element(ForgotInfoElements.TXT_LASTNAME_ERROR)
        self.assertEqual(self.get_text(txt_lastname_error),'Last name is required.')
        txt_street_error = self.find_element(ForgotInfoElements.TXT_STREET_ERROR)
        self.assertEqual(self.get_text(txt_street_error),'Address is required.')
        txt_city_error = self.find_element(ForgotInfoElements.TXT_CITY_ERROR)
        self.assertEqual(self.get_text(txt_city_error),'City is required.')
        txt_state_error = self.find_element(ForgotInfoElements.TXT_STATE_ERROR)
        self.assertEqual(self.get_text(txt_state_error),'State is required.')
        txt_zipcode_error = self.find_element(ForgotInfoElements.TXT_ZIPCODE_ERROR)
        self.assertEqual(self.get_text(txt_zipcode_error),'Zip Code is required.')
        txt_ssn_error = self.find_element(ForgotInfoElements.TXT_SSN_ERROR)
        self.assertEqual(self.get_text(txt_ssn_error),'Social Security Number is required.')
      
if __name__ == '__main__':
    unittest.main()
