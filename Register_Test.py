from page_element.register import RegisterPageElements 
from page_element.register import RegisterPageErrorMessage
from page_element.left_menu import LeftMenuElements
from Common import CommonPage 
import unittest
import json
import time

class RegisterPage(unittest.TestCase):    
    # Pre-condition: before running test, In account_data.json, "Username" should updated with value that is NOT existing in system before
    acc_data = json.load(open('./data/account_data.json'))
    firstnamevalue = acc_data["First Name"]
    lastnamevalue = acc_data["Last Name"]
    usernamevalue = acc_data["Username"]
    passwordvalue = acc_data["Password"]
      
    def test_register_successfully(self):
        common = CommonPage()
        common.setUp()
        common.open_base_url()
        link_register = common.find_element(LeftMenuElements.LINK_REGISTER)
        common.click_button(link_register)
        txt_firstname = common.find_element(
                RegisterPageElements.TXTBOX_FIRSTNAME)
        common.input_text(txt_firstname, self.firstnamevalue)
        txt_lastname = common.find_element(RegisterPageElements.TXTBOX_LASTNAME)
        common.input_text(txt_lastname, self.lastnamevalue)
        txt_street = common.find_element(
                RegisterPageElements.TXTBOX_ADDRESS_STREET)
        common.input_text(txt_street, self.acc_data["Street"])
        txt_city = common.find_element(RegisterPageElements.TXTBOX_ADDRESS_CITY)
        common.input_text(txt_city, self.acc_data["City"])
        txt_state = common.find_element(
                RegisterPageElements.TXTBOX_ADDRESS_STATE)
        common.input_text(txt_state, self.acc_data["State"])
        txt_zipcode = common.find_element(
                RegisterPageElements.TXTBOX_ADDRESS_ZIPCODE)
        common.input_text(txt_zipcode, self.acc_data["Zipcode"])
        txt_phone = common.find_element(RegisterPageElements.TXTBOX_PHONENUMBER)
        common.input_text(txt_phone, self.acc_data["PhoneNumber"])
        txt_ssn = common.find_element(RegisterPageElements.TXTBOX_SSN)
        common.input_text(txt_ssn, self.acc_data["SSN"])
        txt_username = common.find_element(RegisterPageElements.TXTBOX_USERNAME)
        common.input_text(txt_username, self.usernamevalue)
        txt_password = common.find_element(RegisterPageElements.TXTBOX_PASSWORD)
        common.input_text(txt_password, self.passwordvalue)
        txt_confirmpw = common.find_element(
                RegisterPageElements.TXTBOX_CONFIRMPW)
        common.input_text(txt_confirmpw, self.passwordvalue)
        btn_register = common.find_element(RegisterPageElements.BTN_REGISTER)
        common.click_button(btn_register)
        time.sleep(5)
        # Verify account registered successfully
        txt_welcome = common.find_element(RegisterPageElements.TXT_WELCOME)
        self.assertEqual(common.get_text(txt_welcome), 'Welcome ' +
                                   self.usernamevalue, 'Account registered unsuccessfully')
        txt_SuccessMsg = common.find_element(RegisterPageElements.TXT_CREATEDMSG)
        self.assertEqual(common.get_text(txt_SuccessMsg),
                                   'Your account was created successfully. You are now logged in.')
            # Check registered account can login successfully
        link_logout = common.find_element(LeftMenuElements.LINK_LOGOUT)
        common.click_button(link_logout)
        time.sleep(5)
        common.tearDown()

    def test_login_successfully(self):
        common = CommonPage()
        common.login(self.usernamevalue,self.passwordvalue)
        txt_welcomelogin = common.find_element(
                RegisterPageElements.TXT_WELCOMELOGIN)
        self.assertEqual(common.get_text(txt_welcomelogin), 'Welcome ' +
                                   self.firstnamevalue + ' ' + self.lastnamevalue, 'Login unsucessfully')
        time.sleep(5)
        common.tearDown()
    
    def test_register_unsuccessfully(self):
        common = CommonPage()
        common.setUp()
        common.open_base_url()
        link_register = common.find_element(LeftMenuElements.LINK_REGISTER)
        common.click_button(link_register)
        btn_register = common.find_element(RegisterPageElements.BTN_REGISTER)
        common.click_button(btn_register)
        txt_firstname_error = common.find_element(RegisterPageErrorMessage.TXT_FIRSTNAME_ERROR)
        self.assertEqual(common.get_text(txt_firstname_error),'First name is required.')
        txt_lastname_error = common.find_element(RegisterPageErrorMessage.TXT_LASTNAME_ERROR)
        self.assertEqual(common.get_text(txt_lastname_error),'Last name is required.')
        txt_street_error = common.find_element(RegisterPageErrorMessage.TXT_STREET_ERROR)
        self.assertEqual(common.get_text(txt_street_error),'Address is required.')
        txt_city_error = common.find_element(RegisterPageErrorMessage.TXT_CITY_ERROR)
        self.assertEqual(common.get_text(txt_city_error),'City is required.')
        txt_state_error = common.find_element(RegisterPageErrorMessage.TXT_STATE_ERROR)
        self.assertEqual(common.get_text(txt_state_error),'State is required.')
        txt_zipcode_error = common.find_element(RegisterPageErrorMessage.TXT_ZIPCODE_ERROR)
        self.assertEqual(common.get_text(txt_zipcode_error),'Zip Code is required.')
        txt_ssn_error = common.find_element(RegisterPageErrorMessage.TXT_SSN_ERROR)
        self.assertEqual(common.get_text(txt_ssn_error),'Social Security Number is required.')
        txt_username_error = common.find_element(RegisterPageErrorMessage.TXT_USERNAME_ERROR)
        self.assertEqual(common.get_text(txt_username_error),'Username is required.')
        txt_password_error = common.find_element(RegisterPageErrorMessage.TXT_PASSWORD_ERROR)
        self.assertEqual(common.get_text(txt_password_error),'Password is required.')
        txt_confirmpw_error = common.find_element(RegisterPageErrorMessage.TXT_CONFIRMPW_ERROR)
        self.assertEqual(common.get_text(txt_confirmpw_error),'Password confirmation is required.')

        txt_password = common.find_element(RegisterPageElements.TXTBOX_PASSWORD)
        common.input_text(txt_password, '123')
        txt_confirmpw = common.find_element(RegisterPageElements.TXTBOX_CONFIRMPW)
        common.input_text(txt_confirmpw, '456')
        common.click_button(common.find_element(RegisterPageElements.BTN_REGISTER))
        actual_result = common.get_text(common.find_element(RegisterPageErrorMessage.TXT_CONFIRMPW_ERROR))
        self.assertEqual(actual_result,'Passwords did not match.')
        common.tearDown()

def suite():
    suite = unittest.TestSuite()
    suite.addTest(RegisterPage('test_register_successfully'))
    suite.addTest(RegisterPage('test_login_successfully'))
    suite.addTest(RegisterPage('test_register_unsuccessfully'))
    return suite
if __name__ == '__main__':
    runner = unittest.TextTestRunner()
    runner.run(suite())