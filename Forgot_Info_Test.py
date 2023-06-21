import unittest
from page_element.forgot_info import ForgotInfoElements
from page_element.forgot_info import ForgotErrorMsgElements
from page_element.left_menu import LeftMenuElements
from page_element.error_message import ErrorMessages
from Common import CommonPage
import json

class ForgotInfoPage(unittest.TestCase):
    # Pre-condition: Information into account_data.json should be registered successfully by running Register_Test.py
    def test_forgot_successfully(self):
        account = json.load(open('./data/account_data.json'))
        common = CommonPage()
        common.setUp()
        common.open_base_url()
        common.click_button(LeftMenuElements.LINK_FORGOTINFO)
        common.input_text(ForgotInfoElements.TXTBOX_FIRSTNAME, account["First Name"])
        common.input_text(ForgotInfoElements.TXTBOX_LASTNAME, account["Last Name"])
        common.input_text(ForgotInfoElements.TXTBOX_STREET, account["Street"])
        common.input_text(ForgotInfoElements.TXTBOX_CITY, account["City"])
        common.input_text(ForgotInfoElements.TXTBOX_STATE, account["State"])
        common.input_text(ForgotInfoElements.TXTBOX_ZIPCODE, account["Zipcode"])
        common.input_text(ForgotInfoElements.TXTBOX_SSN, account["SSN"])
        common.click_button(ForgotInfoElements.BTN_FINDINFO)
        except_result = "Username: " + account["Username"] + '\n' + "Password: " + account["Password"]
        actual_result = common.get_text(ForgotInfoElements.TXT_USERNAMEPW)
        self.assertEqual(except_result,actual_result)
        common.tearDown()

    def test_validation(self):
        common = CommonPage()
        common.setUp()
        common.open_base_url()
        common.click_button(LeftMenuElements.LINK_FORGOTINFO)
        common.click_button(ForgotInfoElements.BTN_FINDINFO)
        self.assertEqual(common.get_text(ForgotErrorMsgElements.TXT_FIRSTNAME_ERROR),ErrorMessages.FIRSTNAME_ERROR)
        self.assertEqual(common.get_text(ForgotErrorMsgElements.TXT_LASTNAME_ERROR),ErrorMessages.LASTNAME_ERROR)
        self.assertEqual(common.get_text(ForgotErrorMsgElements.TXT_STREET_ERROR),ErrorMessages.STREET_ERROR)
        self.assertEqual(common.get_text(ForgotErrorMsgElements.TXT_CITY_ERROR),ErrorMessages.CITY_ERROR)
        self.assertEqual(common.get_text(ForgotErrorMsgElements.TXT_STATE_ERROR),ErrorMessages.STATE_ERROR)
        self.assertEqual(common.get_text(ForgotErrorMsgElements.TXT_ZIPCODE_ERROR),ErrorMessages.ZIPCODE_ERROR)
        self.assertEqual(common.get_text(ForgotErrorMsgElements.TXT_SSN_ERROR),ErrorMessages.SSN_ERROR)
        common.tearDown()
      
def suite():
    suite = unittest.TestSuite()
    suite.addTest(ForgotInfoPage('test_forgot_successfully'))
    # suite.addTest(ForgotInfoPage('test_validation'))
    return suite       
        
if __name__ == '__main__':
    runner = unittest.TextTestRunner()
    runner.run(suite())
