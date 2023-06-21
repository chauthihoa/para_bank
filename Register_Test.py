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
        common.click_button(LeftMenuElements.LINK_REGISTER)
        common.input_text(RegisterPageElements.TXTBOX_FIRSTNAME, self.firstnamevalue)
        common.input_text(RegisterPageElements.TXTBOX_LASTNAME, self.lastnamevalue)
        common.input_text(RegisterPageElements.TXTBOX_ADDRESS_STREET, self.acc_data["Street"])
        common.input_text(RegisterPageElements.TXTBOX_ADDRESS_CITY, self.acc_data["City"])
        common.input_text(RegisterPageElements.TXTBOX_ADDRESS_STATE, self.acc_data["State"])
        common.input_text(RegisterPageElements.TXTBOX_ADDRESS_ZIPCODE, self.acc_data["Zipcode"])
        common.input_text(RegisterPageElements.TXTBOX_PHONENUMBER, self.acc_data["PhoneNumber"])
        common.input_text(RegisterPageElements.TXTBOX_SSN, self.acc_data["SSN"])
        common.input_text(RegisterPageElements.TXTBOX_USERNAME, self.usernamevalue)
        common.input_text(RegisterPageElements.TXTBOX_PASSWORD, self.passwordvalue)
        common.input_text(RegisterPageElements.TXTBOX_CONFIRMPW, self.passwordvalue)
        common.click_button(RegisterPageElements.BTN_REGISTER)
        time.sleep(5)
        # Verify account registered successfully
        self.assertEqual(common.get_text(RegisterPageElements.TXT_WELCOME), 'Welcome ' +
                                   self.usernamevalue, 'Account registered unsuccessfully')
        self.assertEqual(common.get_text(RegisterPageElements.TXT_CREATEDMSG),
                                   'Your account was created successfully. You are now logged in.')
        # Check registered account can login successfully
        common.click_button(LeftMenuElements.LINK_LOGOUT)
        time.sleep(5)
        common.tearDown()

    def test_login_successfully(self):
        common = CommonPage()
        common.login(self.usernamevalue,self.passwordvalue)
        self.assertEqual(common.get_text(RegisterPageElements.TXT_WELCOMELOGIN), 'Welcome ' +
                                   self.firstnamevalue + ' ' + self.lastnamevalue, 'Login unsucessfully')
        time.sleep(5)
        common.tearDown()
    
    def test_register_unsuccessfully(self):
        common = CommonPage()
        common.setUp()
        common.open_base_url()
        common.click_button(LeftMenuElements.LINK_REGISTER)
        common.click_button(RegisterPageElements.BTN_REGISTER)
        self.assertEqual(common.get_text(RegisterErrorMsgElements.TXT_FIRSTNAME_ERROR),ErrorMessages.FIRSTNAME_ERROR)
        self.assertEqual(common.get_text(RegisterErrorMsgElements.TXT_LASTNAME_ERROR),ErrorMessages.LASTNAME_ERROR)
        self.assertEqual(common.get_text(RegisterErrorMsgElements.TXT_STREET_ERROR),ErrorMessages.STREET_ERROR)
        self.assertEqual(common.get_text(RegisterErrorMsgElements.TXT_CITY_ERROR),ErrorMessages.CITY_ERROR)
        self.assertEqual(common.get_text(RegisterErrorMsgElements.TXT_STATE_ERROR),ErrorMessages.STATE_ERROR)
        self.assertEqual(common.get_text(RegisterErrorMsgElements.TXT_ZIPCODE_ERROR),ErrorMessages.ZIPCODE_ERROR)
        self.assertEqual(common.get_text(RegisterErrorMsgElements.TXT_SSN_ERROR),ErrorMessages.SSN_ERROR)
        self.assertEqual(common.get_text(RegisterErrorMsgElements.TXT_USERNAME_ERROR),ErrorMessages.USERNAME_ERROR)
        self.assertEqual(common.get_text(RegisterErrorMsgElements.TXT_PASSWORD_ERROR),ErrorMessages.PASSWORD_ERROR)
        self.assertEqual(common.get_text(RegisterErrorMsgElements.TXT_CONFIRMPW_ERROR),ErrorMessages.CONFIRMPW_1_ERROR)

        common.input_text(RegisterPageElements.TXTBOX_PASSWORD, '123')
        common.input_text(RegisterPageElements.TXTBOX_CONFIRMPW, '456')
        common.click_button(RegisterPageElements.BTN_REGISTER)
        actual_result = common.get_text(RegisterErrorMsgElements.TXT_CONFIRMPW_ERROR)
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