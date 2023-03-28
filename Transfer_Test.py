from selenium.webdriver.support.select import Select
from page_element.transfer import TransferElements
from page_element.left_menu import LeftMenuElements
from Common import CommonPage
import unittest
import json
import time


class TransferPage(unittest.TestCase):
    # Pre-condition: Information into account_data.json should be registered successfully by running Register_Test.py    
    def test_transfer_successfully(self):
        acc_data = json.load(open('./data/account_data.json'))
        #Login
        common = CommonPage()
        common.login(acc_data["Username"],acc_data["Password"])

        #Open new account
        link_opennewaccount = common.find_element(LeftMenuElements.LINK_OPENNEWACC)
        common.click_button(link_opennewaccount)
        time.sleep(10)
        dropdown_accfrom = Select(common.find_element(TransferElements.DROPDOWN_ACCFROM)).first_selected_option
        firstAccountID = dropdown_accfrom.text
        btn_opennewaccount = common.find_element(TransferElements.BTN_OPENNEWACC)
        common.click_button(btn_opennewaccount)
        time.sleep(10)
        txt_newaccountid = common.find_element(TransferElements.TXT_NEWACCID)
        secondAccountID =  common.get_text(txt_newaccountid)

        #Get available amount of 2 accounts
        link_accountoverview = common.find_element(LeftMenuElements.LINK_ACCOUNTSOVERVIEW)
        common.click_button(link_accountoverview)
        time.sleep(5)
        txt_availableamount_1 = common.find_element(TransferElements.TXT_AVAILABLEAMOUNT_1)
        expected_amount_1 = float(common.get_text(txt_availableamount_1).lstrip('$'))
        txt_availableamount_2 = common.find_element(TransferElements.TXT_AVAILABLEAMOUNT_2)
        expected_amount_2 = float(common.get_text(txt_availableamount_2).lstrip('$'))

        #Transfer Fun for Account 1
        link_transferfun = common.find_element(LeftMenuElements.LINK_TRANSFERFUN)
        common.click_button(link_transferfun)
        time.sleep(5)
        transfer_amount_1 = '50'
        txt_amount = common.find_element(TransferElements.TXTBOX_AMOUNT)
        common.input_text(txt_amount,transfer_amount_1)
        fromAcc = Select(common.find_element(TransferElements.DROPDOWN_ACCFROM))
        common.select_option(fromAcc,firstAccountID)
        toAcc = Select(common.find_element(TransferElements.DROPDOWN_ACCTO))
        common.select_option(toAcc,secondAccountID)
        btn_transfer = common.find_element(TransferElements.BTN_TRANSFER)
        common.click_button(btn_transfer)

        #Check amount_1 and amount_2 after transfering
        link_accountoverview = common.find_element(LeftMenuElements.LINK_ACCOUNTSOVERVIEW)
        common.click_button(link_accountoverview)
        time.sleep(5)
        txt_availableamount_1 = common.find_element(TransferElements.TXT_AVAILABLEAMOUNT_1)
        actual_amount_1 = float(common.get_text(txt_availableamount_1).lstrip('$'))
        txt_availableamount_2 = common.find_element(TransferElements.TXT_AVAILABLEAMOUNT_2)
        actual_amount_2 = float(common.get_text(txt_availableamount_2).lstrip('$'))
        self.assertEqual(actual_amount_1,(expected_amount_1 - float(transfer_amount_1)))
        expected_amount_1 = expected_amount_1 - float(transfer_amount_1)
        expected_amount_2 = expected_amount_2 + float(transfer_amount_1)
        self.assertEqual(actual_amount_2,expected_amount_2)

        #Transfer Fun for Account 2
        link_transferfun = common.find_element(LeftMenuElements.LINK_TRANSFERFUN)
        common.click_button(link_transferfun)
        time.sleep(5)
        transfer_amount_2 = '25'
        txt_amount = common.find_element(TransferElements.TXTBOX_AMOUNT)
        common.input_text(txt_amount,transfer_amount_2)
        fromAcc = Select(common.find_element(TransferElements.DROPDOWN_ACCFROM))
        common.select_option(fromAcc,secondAccountID)
        toAcc = Select(common.find_element(TransferElements.DROPDOWN_ACCTO))
        common.select_option(toAcc,firstAccountID)
        btn_transfer = common.find_element(TransferElements.BTN_TRANSFER)
        common.click_button(btn_transfer)

        #Check amount_1 and amount_2 after transfering
        link_accountoverview = common.find_element(LeftMenuElements.LINK_ACCOUNTSOVERVIEW)
        common.click_button(link_accountoverview)
        time.sleep(5)
        txt_availableamount_1 = common.find_element(TransferElements.TXT_AVAILABLEAMOUNT_1)
        actual_amount_1 = float(common.get_text(txt_availableamount_1).lstrip('$'))
        txt_availableamount_2 = common.find_element(TransferElements.TXT_AVAILABLEAMOUNT_2)
        actual_amount_2 = float(common.get_text(txt_availableamount_2).lstrip('$'))
        self.assertEqual(actual_amount_2,(expected_amount_2 - float(transfer_amount_2)))
        expected_amount_1 = expected_amount_1 + float(transfer_amount_2)
        self.assertEqual(actual_amount_1,expected_amount_1)
        common.tearDown()

if __name__ == '__main__':
    unittest.main()

