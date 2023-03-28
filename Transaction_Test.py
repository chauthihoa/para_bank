from selenium.webdriver.support.select import Select
from Common import CommonPage
from page_element.left_menu import LeftMenuElements
from page_element.transaction import TransactionElements
import unittest
import json
import time
import datetime

class TransactionPage(unittest.TestCase):
    acc_data = json.load(open('./data/account_data.json'))

    def test_findTransactionByID(self):
        common = CommonPage()
        common.login(self.acc_data["Username"],self.acc_data["Password"])
        link_accountoverview = common.find_element(LeftMenuElements.LINK_ACCOUNTSOVERVIEW)
        common.click_button(link_accountoverview)
        time.sleep(5)
        link_availableamout_1 = common.find_element(TransactionElements.LINK_AVAILABLEAMOUNT_1)
        common.click_button(link_availableamout_1)
        time.sleep(5)
        link_transaction = common.find_element(TransactionElements.LINK_TRANSACTION)
        common.click_button(link_transaction)
        txt_transactionid = common.find_element(TransactionElements.TXT_TRANSACTIONID)
        expected_transactionid = common.get_text(txt_transactionid)
        txt_date = common.find_element(TransactionElements.TXT_DATE)
        expected_date = common.get_text(txt_date)
        txt_description = common.find_element(TransactionElements.TXT_DESCRIPTION)
        expected_description = common.get_text(txt_description)
        txt_type = common.find_element(TransactionElements.TXT_TYPE)
        expected_type = common.get_text(txt_type)
        txt_amount = common.find_element(TransactionElements.TXT_AMOUNT)
        expected_amount = common.get_text(txt_amount)

        link_findtransaction = common.find_element(LeftMenuElements.LINK_FINDTRANSACTION)
        common.click_button(link_findtransaction)
        txt_criteriatransactionid = common.find_element(TransactionElements.TXT_CRITERIATRANSACTIONID)
        common.input_text(txt_criteriatransactionid,expected_transactionid)
        btn_findtransaction = common.find_element(TransactionElements.BTN_FINDTRANSACTIONBYID)
        common.click_button(btn_findtransaction)
        time.sleep(5)
        link_transaction = common.find_element(TransactionElements.LINK_TRANSACTION)
        common.click_button(link_transaction)
        time.sleep(5)
        txt_transactionid = common.find_element(TransactionElements.TXT_TRANSACTIONID)
        actual_transactionid = common.get_text(txt_transactionid)
        txt_date = common.find_element(TransactionElements.TXT_DATE)
        actual_date = common.get_text(txt_date)
        txt_description = common.find_element(TransactionElements.TXT_DESCRIPTION)
        actual_description = common.get_text(txt_description)
        txt_type = common.find_element(TransactionElements.TXT_TYPE)
        actual_type = common.get_text(txt_type)
        txt_amount = common.find_element(TransactionElements.TXT_AMOUNT)
        actual_amount = common.get_text(txt_amount)
        self.assertEqual(expected_transactionid,actual_transactionid)
        self.assertEqual(expected_date,actual_date)
        self.assertEqual(expected_description,actual_description)
        self.assertEqual(expected_type,actual_type)
        self.assertEqual(expected_amount,actual_amount)
        common.tearDown()

    def test_findTransactionByDate(self):
        today_date = datetime.date.today().strftime("%m-%d-%Y")
        common = CommonPage()
        common.login(self.acc_data["Username"],self.acc_data["Password"])
        link_accountoverview = common.find_element(LeftMenuElements.LINK_ACCOUNTSOVERVIEW)
        common.click_button(link_accountoverview)
        time.sleep(5)
        link_availableamout_2 = common.find_element(TransactionElements.LINK_AVAILABLEAMOUNT_2)
        account = common.get_text(link_availableamout_2)
        common.click_button(link_availableamout_2)
        time.sleep(5)
        txt_transactiondate = common.find_elements(TransactionElements.TXT_TRANSACTIONDATE.format(param=today_date))
        expected_numbertransaction = len(txt_transactiondate) 
        link_findtransaction = common.find_element(LeftMenuElements.LINK_FINDTRANSACTION)
        common.click_button(link_findtransaction)
        dropdown_account = Select(common.find_element(TransactionElements.DROPDOWN_ACCOUNTID))
        common.select_option(dropdown_account,account)
        txt_criteriatransactionid = common.find_element(TransactionElements.TXT_CRITERIAONDATE)
        common.input_text(txt_criteriatransactionid,today_date)
        btn_findtransaction = common.find_element(TransactionElements.BTN_FINDTRANSACTIONBYDATE)
        common.click_button(btn_findtransaction)
        time.sleep(5)
        txt_transactiondate = common.find_elements(TransactionElements.TXT_TRANSACTIONDATE.format(param=today_date))
        actual_numbertransaction = len(txt_transactiondate)
        self.assertEqual(expected_numbertransaction,actual_numbertransaction)
        common.tearDown()

def suite():
    suite = unittest.TestSuite()
    suite.addTest(TransactionPage('test_findTransactionByID'))
    suite.addTest(TransactionPage('test_findTransactionByDate'))
    return suite
        
if __name__ == '__main__':
    runner = unittest.TextTestRunner()
    runner.run(suite())