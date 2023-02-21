from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
import unittest
import json
from page_element.Register import RegisterPageElements 

class RegisterPage(unittest.TestCase):    
    # Pre-condition: before running test, In account_data.json, "Username" should updated with value that is NOT existing in system before
    f = open('./data/account_data.json')
    acc_data = json.load(f)
    f.close()
    def setUp(self):
        self.drive = self.drive = webdriver.Chrome()

    def open_base_url(self, url='https://parabank.parasoft.com/'):
        self.drive.get(url)

    def find_element(self, ele: str):
        return self.drive.find_element(By.XPATH, ele)

    def input_text(self, ele: WebElement, txt: str):
        return ele.send_keys(txt)

    def click_button(self, ele: WebElement):
        return ele.click()

    def get_text(self, ele: WebElement):
        return ele.text
    def test_register_successfully(self):
        self.open_base_url()
        
        firstnamevalue = self.acc_data["First Name"]
        lastnamevalue = self.acc_data["Last Name"]
        usernamevalue = self.acc_data["Username"]
        passwordvalue = self.acc_data["Password"]
        link_register = self.find_element(RegisterPageElements.LINK_REGISTER)
        self.click_button(link_register)
        txt_firstname = self.find_element(
            RegisterPageElements.TXTBOX_FIRSTNAME)
        self.input_text(txt_firstname, firstnamevalue)
        txt_lastname = self.find_element(RegisterPageElements.TXTBOX_LASTNAME)
        self.input_text(txt_lastname, lastnamevalue)
        txt_street = self.find_element(
            RegisterPageElements.TXTBOX_ADDRESS_STREET)
        self.input_text(txt_street, self.acc_data["Street"])
        txt_city = self.find_element(RegisterPageElements.TXTBOX_ADDRESS_CITY)
        self.input_text(txt_city, self.acc_data["City"])
        txt_state = self.find_element(
            RegisterPageElements.TXTBOX_ADDRESS_STATE)
        self.input_text(txt_state, self.acc_data["State"])
        txt_zipcode = self.find_element(
            RegisterPageElements.TXTBOX_ADDRESS_ZIPCODE)
        self.input_text(txt_zipcode, self.acc_data["Zipcode"])
        txt_phone = self.find_element(RegisterPageElements.TXTBOX_PHONENUMBER)
        self.input_text(txt_phone, self.acc_data["PhoneNumber"])
        txt_ssn = self.find_element(RegisterPageElements.TXTBOX_SSN)
        self.input_text(txt_ssn, self.acc_data["SSN"])
        txt_username = self.find_element(RegisterPageElements.TXTBOX_USERNAME)
        self.input_text(txt_username, usernamevalue)
        txt_password = self.find_element(RegisterPageElements.TXTBOX_PASSWORD)
        self.input_text(txt_password, passwordvalue)
        txt_confirmpw = self.find_element(
            RegisterPageElements.TXTBOX_CONFIRMPW)
        self.input_text(txt_confirmpw, passwordvalue)
        btn_register = self.find_element(RegisterPageElements.BTN_REGISTER)
        self.click_button(btn_register)
        # Verify account registered successfully
        txt_welcome = self.find_element(RegisterPageElements.TXT_WELCOME)
        self.assertEqual(self.get_text(txt_welcome), 'Welcome ' +
                               usernamevalue, 'Account registered unsuccessfully')
        txt_SuccessMsg = self.find_element(RegisterPageElements.TXT_CREATEDMSG)
        self.assertEqual(self.get_text(txt_SuccessMsg),
                               'Your account was created successfully. You are now logged in.')
        # Check registered account can login successfully
        link_logout = self.find_element(RegisterPageElements.LINK_LOGOUT)
        self.click_button(link_logout)
        txt_usernamelogin = self.find_element(
            RegisterPageElements.TXTBOX_USERNAMELOGIN)
        self.input_text(txt_usernamelogin, usernamevalue)
        txt_passwordlogin = self.find_element(
            RegisterPageElements.TXTBOX_PASSWORDLOGIN)
        self.input_text(txt_passwordlogin, passwordvalue)
        btn_login = self.find_element(RegisterPageElements.BTN_LOGIN)
        self.click_button(btn_login)
        txt_welcomelogin = self.find_element(
            RegisterPageElements.TXT_WELCOMELOGIN)
        self.assertEqual(self.get_text(txt_welcomelogin), 'Welcome ' +
                               firstnamevalue + ' ' + lastnamevalue, 'Login unsucessfully')
        self.drive.close()

    def test_register_unsuccessfully(self):
        self.open_base_url()
        link_register = self.find_element(RegisterPageElements.LINK_REGISTER)
        self.click_button(link_register)
        btn_register = self.find_element(RegisterPageElements.BTN_REGISTER)
        self.click_button(btn_register)
        txt_firstname_error = self.find_element(RegisterPageElements.TXT_FIRSTNAME_ERROR)
        self.assertEqual(self.get_text(txt_firstname_error),'First name is required.')
        txt_lastname_error = self.find_element(RegisterPageElements.TXT_LASTNAME_ERROR)
        self.assertEqual(self.get_text(txt_lastname_error),'Last name is required.')
        txt_street_error = self.find_element(RegisterPageElements.TXT_STREET_ERROR)
        self.assertEqual(self.get_text(txt_street_error),'Address is required.')
        txt_city_error = self.find_element(RegisterPageElements.TXT_CITY_ERROR)
        self.assertEqual(self.get_text(txt_city_error),'City is required.')
        txt_state_error = self.find_element(RegisterPageElements.TXT_STATE_ERROR)
        self.assertEqual(self.get_text(txt_state_error),'State is required.')
        txt_zipcode_error = self.find_element(RegisterPageElements.TXT_ZIPCODE_ERROR)
        self.assertEqual(self.get_text(txt_zipcode_error),'Zip Code is required.')
        txt_ssn_error = self.find_element(RegisterPageElements.TXT_SSN_ERROR)
        self.assertEqual(self.get_text(txt_ssn_error),'Social Security Number is required.')
        txt_username_error = self.find_element(RegisterPageElements.TXT_USERNAME_ERROR)
        self.assertEqual(self.get_text(txt_username_error),'Username is required.')
        txt_password_error = self.find_element(RegisterPageElements.TXT_PASSWORD_ERROR)
        self.assertEqual(self.get_text(txt_password_error),'Password is required.')
        txt_confirmpw_error = self.find_element(RegisterPageElements.TXT_CONFIRMPW_ERROR)
        self.assertEqual(self.get_text(txt_confirmpw_error),'Password confirmation is required.')

        txt_password = self.find_element(RegisterPageElements.TXTBOX_PASSWORD)
        self.input_text(txt_password, '123')
        txt_confirmpw = self.find_element(RegisterPageElements.TXTBOX_CONFIRMPW)
        self.input_text(txt_confirmpw, '456')
        self.click_button(self.find_element(RegisterPageElements.BTN_REGISTER))
        actual_result = self.get_text(self.find_element(RegisterPageElements.TXT_CONFIRMPW_ERROR))
        self.assertEqual(actual_result,'Passwords did not match.')

if __name__ == '__main__':
    unittest.main()