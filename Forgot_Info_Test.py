import unittest
from page_element.forgot_info import ForgotInfoElements
from page_element.forgot_info import ForgotPageErrorMessage
from page_element.left_menu import LeftMenuElements
from Common import CommonPage
import json

class ForgotInfoPage(unittest.TestCase):
    # Pre-condition: Information into account_data.json should be registered successfully by running Register_Test.py
    def test_forgot_successfully(self):
        account = json.load(open('./data/account_data.json'))
        common = CommonPage()
        common.setUp()
        common.open_base_url()
        link_forgotinfo = common.find_element(LeftMenuElements.LINK_FORGOTINFO)
        common.click_button(link_forgotinfo)
        txt_firstname = common.find_element(ForgotInfoElements.TXTBOX_FIRSTNAME)
        common.input_text(txt_firstname, account["First Name"])
        txt_lastname = common.find_element(ForgotInfoElements.TXTBOX_LASTNAME)
        common.input_text(txt_lastname, account["Last Name"])
        txt_street = common.find_element(ForgotInfoElements.TXTBOX_STREET)
        common.input_text(txt_street, account["Street"])
        txt_city = common.find_element(ForgotInfoElements.TXTBOX_CITY)
        common.input_text(txt_city, account["City"])
        txt_state = common.find_element(ForgotInfoElements.TXTBOX_STATE)
        common.input_text(txt_state, account["State"])
        txt_zipcode = common.find_element(ForgotInfoElements.TXTBOX_ZIPCODE)
        common.input_text(txt_zipcode, account["Zipcode"])
        txt_ssn = common.find_element(ForgotInfoElements.TXTBOX_SSN)
        common.input_text(txt_ssn, account["SSN"])
        btn_findinfo = common.find_element(ForgotInfoElements.BTN_FINDINFO)
        common.click_button(btn_findinfo)
        except_result = "Username: " + account["Username"] + '\n' + "Password: " + account["Password"]
        actual_result = common.find_element(ForgotInfoElements.TXT_USERNAMEPW)
        self.assertEqual(except_result,common.get_text(actual_result))
        common.tearDown()

    def test_validation(self):
        common = CommonPage()
        common.setUp()
        common.open_base_url()
        link_forgotinfo = common.find_element(LeftMenuElements.LINK_FORGOTINFO)
        common.click_button(link_forgotinfo)
        btn_findinfo = common.find_element(ForgotInfoElements.BTN_FINDINFO)
        common.click_button(btn_findinfo)
        txt_firstname_error = common.find_element(ForgotPageErrorMessage.TXT_FIRSTNAME_ERROR)
        self.assertEqual(common.get_text(txt_firstname_error),'First name is required.')
        txt_lastname_error = common.find_element(ForgotPageErrorMessage.TXT_LASTNAME_ERROR)
        self.assertEqual(common.get_text(txt_lastname_error),'Last name is required.')
        txt_street_error = common.find_element(ForgotPageErrorMessage.TXT_STREET_ERROR)
        self.assertEqual(common.get_text(txt_street_error),'Address is required.')
        txt_city_error = common.find_element(ForgotPageErrorMessage.TXT_CITY_ERROR)
        self.assertEqual(common.get_text(txt_city_error),'City is required.')
        txt_state_error = common.find_element(ForgotPageErrorMessage.TXT_STATE_ERROR)
        self.assertEqual(common.get_text(txt_state_error),'State is required.')
        txt_zipcode_error = common.find_element(ForgotPageErrorMessage.TXT_ZIPCODE_ERROR)
        self.assertEqual(common.get_text(txt_zipcode_error),'Zip Code is required.')
        txt_ssn_error = common.find_element(ForgotPageErrorMessage.TXT_SSN_ERROR)
        self.assertEqual(common.get_text(txt_ssn_error),'Social Security Number is required.')
        common.tearDown()
      
def suite():
    suite = unittest.TestSuite()
    suite.addTest(ForgotInfoPage('test_forgot_successfully'))
    suite.addTest(ForgotInfoPage('test_validation'))
    return suite       
        
if __name__ == '__main__':
    runner = unittest.TextTestRunner()
    runner.run(suite())
