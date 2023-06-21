from selenium.webdriver.support.select import Select
from page_element.transfer import TransferElements
from page_element.left_menu import LeftMenuElements
from Common import CommonPage
import unittest
import json
import time
import re


class TransferPage(unittest.TestCase):
    # Pre-condition: Information into account_data.json should be registered successfully by running Register_Test.py    
    def test_transfer_successfully(self):
        acc_data = json.load(open('./data/account_data.json'))
        transfer_amount_1 = input("Enter transfer amount 1(1 <= value <= 100): ")
        transfer_amount_2 = input("Enter transfer amount 2(1 <= value <= 100): ")
        if(bool(float(transfer_amount_1)) and bool(float(transfer_amount_1))):
            amount_1 = float(transfer_amount_1)
            amount_2 = float(transfer_amount_2)
            common = CommonPage()
            if(common.is_value_inrange(amount_1,1,100) and common.is_value_inrange(amount_2,1,100)):
                #Login
                common.login(acc_data["Username"],acc_data["Password"])

                #Open new account
                common.click_button(LeftMenuElements.LINK_OPENNEWACC)
                time.sleep(10)
                dropdown_accfrom = Select(common.find_element(TransferElements.DROPDOWN_ACCFROM)).first_selected_option
                firstAccountID = dropdown_accfrom.text
                common.click_button(TransferElements.BTN_OPENNEWACC)
                time.sleep(10)
                txt_newaccountid = common.find_element(TransferElements.TXT_NEWACCID)
                secondAccountID =  common.get_text(txt_newaccountid)

                #Get available amount of 2 accounts
                common.click_button(LeftMenuElements.LINK_ACCOUNTSOVERVIEW)
                time.sleep(5)
                txt_availableamount_1 = common.find_element(TransferElements.TXT_AVAILABLEAMOUNT_1)
                # expected_amount_1 = float(common.get_text(txt_availableamount_1).lstrip('$'))
                expected_amount_1 = float(re.split(r'(\d+)',common.get_text(txt_availableamount_1))[0])
                txt_availableamount_2 = common.find_element(TransferElements.TXT_AVAILABLEAMOUNT_2)
                # expected_amount_2 = float(common.get_text(txt_availableamount_2).lstrip('$'))
                expected_amount_2 = float(re.split(r'(\d+)',common.get_text(txt_availableamount_2))[0])

                #Transfer Fun for Account 1
                common.click_button(LeftMenuElements.LINK_TRANSFERFUN)
                time.sleep(5)
                txt_amount = common.find_element(TransferElements.TXTBOX_AMOUNT)
                common.input_text(txt_amount,transfer_amount_1)
                fromAcc = Select(common.find_element(TransferElements.DROPDOWN_ACCFROM))
                common.select_option(fromAcc,firstAccountID)
                toAcc = Select(common.find_element(TransferElements.DROPDOWN_ACCTO))
                common.select_option(toAcc,secondAccountID)
                common.click_button(TransferElements.BTN_TRANSFER)

                #Check amount_1 and amount_2 after transfering
                common.click_button(LeftMenuElements.LINK_ACCOUNTSOVERVIEW)
                time.sleep(5)
                txt_availableamount_1 = common.find_element(TransferElements.TXT_AVAILABLEAMOUNT_1)
                # actual_amount_1 = float(common.get_text(txt_availableamount_1).lstrip('$'))
                actual_amount_1 = float(re.split(r'(\d+)',common.get_text(txt_availableamount_1))[0])
                txt_availableamount_2 = common.find_element(TransferElements.TXT_AVAILABLEAMOUNT_2)
                # actual_amount_2 = float(common.get_text(txt_availableamount_2).lstrip('$'))
                actual_amount_2 = float(re.split(r'(\d+)',common.get_text(txt_availableamount_2))[0])
                self.assertEqual(actual_amount_1,(expected_amount_1 - amount_1))
                expected_amount_1 = expected_amount_1 - amount_1
                expected_amount_2 = expected_amount_2 + amount_1
                self.assertEqual(actual_amount_2,expected_amount_2)

                #Transfer Fun for Account 2
                common.click_button(LeftMenuElements.LINK_TRANSFERFUN)
                time.sleep(5)
                txt_amount = common.find_element(TransferElements.TXTBOX_AMOUNT)
                common.input_text(txt_amount,transfer_amount_2)
                fromAcc = Select(common.find_element(TransferElements.DROPDOWN_ACCFROM))
                common.select_option(fromAcc,secondAccountID)
                toAcc = Select(common.find_element(TransferElements.DROPDOWN_ACCTO))
                common.select_option(toAcc,firstAccountID)
                common.click_button(TransferElements.BTN_TRANSFER)

                #Check amount_1 and amount_2 after transfering
                common.click_button(LeftMenuElements.LINK_ACCOUNTSOVERVIEW)
                time.sleep(5)
                txt_availableamount_1 = common.find_element(TransferElements.TXT_AVAILABLEAMOUNT_1)
                # actual_amount_1 = float(common.get_text(txt_availableamount_1).lstrip('$'))
                actual_amount_1 = float(re.split(r'(\d+)',common.get_text(txt_availableamount_1))[0])
                txt_availableamount_2 = common.find_element(TransferElements.TXT_AVAILABLEAMOUNT_2)
                # actual_amount_2 = float(common.get_text(txt_availableamount_2).lstrip('$'))
                actual_amount_2 = float(re.split(r'(\d+)',common.get_text(txt_availableamount_2))[0])
                self.assertEqual(actual_amount_2,(expected_amount_2 - amount_2))
                expected_amount_1 = expected_amount_1 + amount_2
                self.assertEqual(actual_amount_1,expected_amount_1)
                common.tearDown()

if __name__ == '__main__':
    unittest.main()