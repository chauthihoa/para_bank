from page_element.register import RegisterPageElements 
from page_element.register import RegisterErrorMsgElements
from page_element.left_menu import LeftMenuElements
from page_element.error_message import ErrorMessages
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
        txt_firstname_error = common.find_element(RegisterErrorMsgElements.TXT_FIRSTNAME_ERROR)
        self.assertEqual(common.get_text(txt_firstname_error),ErrorMessages.FIRSTNAME_ERROR)
        txt_lastname_error = common.find_element(RegisterErrorMsgElements.TXT_LASTNAME_ERROR)
        self.assertEqual(common.get_text(txt_lastname_error),ErrorMessages.LASTNAME_ERROR)
        txt_street_error = common.find_element(RegisterErrorMsgElements.TXT_STREET_ERROR)
        self.assertEqual(common.get_text(txt_street_error),ErrorMessages.STREET_ERROR)
        txt_city_error = common.find_element(RegisterErrorMsgElements.TXT_CITY_ERROR)
        self.assertEqual(common.get_text(txt_city_error),ErrorMessages.CITY_ERROR)
        txt_state_error = common.find_element(RegisterErrorMsgElements.TXT_STATE_ERROR)
        self.assertEqual(common.get_text(txt_state_error),ErrorMessages.STATE_ERROR)
        txt_zipcode_error = common.find_element(RegisterErrorMsgElements.TXT_ZIPCODE_ERROR)
        self.assertEqual(common.get_text(txt_zipcode_error),ErrorMessages.ZIPCODE_ERROR)
        txt_ssn_error = common.find_element(RegisterErrorMsgElements.TXT_SSN_ERROR)
        self.assertEqual(common.get_text(txt_ssn_error),ErrorMessages.SSN_ERROR)
        txt_username_error = common.find_element(RegisterErrorMsgElements.TXT_USERNAME_ERROR)
        self.assertEqual(common.get_text(txt_username_error),ErrorMessages.USERNAME_ERROR)
        txt_password_error = common.find_element(RegisterErrorMsgElements.TXT_PASSWORD_ERROR)
        self.assertEqual(common.get_text(txt_password_error),ErrorMessages.PASSWORD_ERROR)
        txt_confirmpw_error = common.find_element(RegisterErrorMsgElements.TXT_CONFIRMPW_ERROR)
        self.assertEqual(common.get_text(txt_confirmpw_error),ErrorMessages.CONFIRMPW_1_ERROR)

        txt_password = common.find_element(RegisterPageElements.TXTBOX_PASSWORD)
        common.input_text(txt_password, '123')
        txt_confirmpw = common.find_element(RegisterPageElements.TXTBOX_CONFIRMPW)
        common.input_text(txt_confirmpw, '456')
        common.click_button(common.find_element(RegisterPageElements.BTN_REGISTER))
        actual_result = common.get_text(common.find_element(RegisterErrorMsgElements.TXT_CONFIRMPW_ERROR))
        self.assertEqual(actual_result,ErrorMessages.CONFIRMPW_2_ERROR)
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