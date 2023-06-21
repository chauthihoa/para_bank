from selenium.webdriver.support.select import Select
from Common import CommonPage
from page_element.left_menu import LeftMenuElements
from page_element.transaction import TransactionElements
import unittest
import json
import time
from datetime import datetime


class TransactionPage(unittest.TestCase):
    acc_data = json.load(open('./data/account_data.json'))

    def test_findTransactionByID(self):
        common = CommonPage()
        common.login(self.acc_data["Username"], self.acc_data["Password"])
        common.click_button(LeftMenuElements.LINK_ACCOUNTSOVERVIEW)
        time.sleep(5)
        common.click_button(TransactionElements.LINK_AVAILABLEAMOUNT_1)
        time.sleep(5)
        common.click_button(TransactionElements.LINK_TRANSACTION)
        txt_transactionid = common.find_element(
            TransactionElements.TXT_TRANSACTIONID)
        expected_transactionid = common.get_text(txt_transactionid)
        txt_date = common.find_element(TransactionElements.TXT_DATE)
        expected_date = common.get_text(txt_date)
        txt_description = common.find_element(
            TransactionElements.TXT_DESCRIPTION)
        expected_description = common.get_text(txt_description)
        txt_type = common.find_element(TransactionElements.TXT_TYPE)
        expected_type = common.get_text(txt_type)
        txt_amount = common.find_element(TransactionElements.TXT_AMOUNT)
        expected_amount = common.get_text(txt_amount)
        common.click_button(LeftMenuElements.LINK_FINDTRANSACTION)
        txt_criteriatransactionid = common.find_element(
            TransactionElements.TXT_CRITERIATRANSACTIONID)
        common.input_text(txt_criteriatransactionid, expected_transactionid)
        common.click_button(TransactionElements.BTN_FINDTRANSACTIONBYID)
        time.sleep(5)
        common.click_button(TransactionElements.LINK_TRANSACTION)
        time.sleep(5)
        txt_transactionid = common.find_element(
            TransactionElements.TXT_TRANSACTIONID)
        actual_transactionid = common.get_text(txt_transactionid)
        txt_date = common.find_element(TransactionElements.TXT_DATE)
        actual_date = common.get_text(txt_date)
        txt_description = common.find_element(
            TransactionElements.TXT_DESCRIPTION)
        actual_description = common.get_text(txt_description)
        txt_type = common.find_element(TransactionElements.TXT_TYPE)
        actual_type = common.get_text(txt_type)
        txt_amount = common.find_element(TransactionElements.TXT_AMOUNT)
        actual_amount = common.get_text(txt_amount)
        self.assertEqual(expected_transactionid, actual_transactionid)
        self.assertEqual(expected_date, actual_date)
        self.assertEqual(expected_description, actual_description)
        self.assertEqual(expected_type, actual_type)
        self.assertEqual(expected_amount, actual_amount)
        common.tearDown()

    def test_findTransactionByDateRange(self):
        common = CommonPage()
        fromDate = input("Enter FromDate value(mm-dd-yyyy): ")
        toDate = input("Enter ToDate value(mm-dd-yyyy): ")
        if common.is_date_matching(fromDate):
            fromDateValue = datetime.strptime(fromDate, "%m-%d-%Y")
            if common.is_date_matching(toDate):
                toDateValue = datetime.strptime(toDate, "%m-%d-%Y")
                if fromDateValue <= toDateValue and (toDateValue - fromDateValue).days >= 31:
                   self.findTransaction(fromDateValue, toDateValue)
                else:
                    print("Duration(todate - fromdate) < 31 days.")
            else:
                todayDate = datetime.strptime(datetime.today().strftime("%m-%d-%Y"),("%m-%d-%Y"))
                if fromDateValue <= todayDate and (todayDate - fromDateValue).days >= 31:
                    self.findTransaction(fromDateValue,todayDate)
                else:
                    print("Duration(today - date) < 31 days.")
        else:
            print("User input incorrect FromDate and ToDate")

    def findTransaction(self, fromDate: datetime, toDate: datetime):
        common = CommonPage()
        common.login(self.acc_data["Username"], self.acc_data["Password"])
        common.click_button(LeftMenuElements.LINK_ACCOUNTSOVERVIEW)
        time.sleep(5)
        account = common.get_text(common.find_element(TransactionElements.LINK_AVAILABLEAMOUNT_2))
        common.click_button(TransactionElements.LINK_AVAILABLEAMOUNT_2)
        time.sleep(5)
        txt_transactiondate = common.find_elements(
            TransactionElements.TXT_TRANSACTIONDATE)
        count = 0
        for transactionDateItem in txt_transactiondate:
            if common.is_date_matching(transactionDateItem):
                if fromDate <= datetime.strptime(common.get_text(transactionDateItem), "%m-%d-%Y") <= toDate:
                    count += 1
        common.click_button(LeftMenuElements.LINK_FINDTRANSACTION)
        time.sleep(5)
        dropdown_account = Select(common.find_element(
            TransactionElements.DROPDOWN_ACCOUNTID))
        common.select_option(dropdown_account, account)
        txt_criteriatransactionfromdate = common.find_element(
            TransactionElements.TXT_CRITERIAFROMDATE)
        common.input_text(txt_criteriatransactionfromdate,
                          fromDate.date().strftime("%m-%d-%Y"))
        txt_criteriatransactiontodate = common.find_element(
            TransactionElements.TXT_CRITERIATODATE)
        common.input_text(txt_criteriatransactiontodate,
                          toDate.date().strftime("%m-%d-%Y"))
        common.click_button(TransactionElements.BTN_FINDTRANSACTIONBYDATERANGE)
        time.sleep(5)
        txt_transactiondate = common.find_elements(
            TransactionElements.TXT_TRANSACTIONDATE)
        for transactionDateItem in txt_transactiondate:
            print(type(transactionDateItem))
        self.assertEqual(count, len(txt_transactiondate))
        common.tearDown()


def suite():
    suite = unittest.TestSuite()
    suite.addTest(TransactionPage('test_findTransactionByDateRange'))
    suite.addTest(TransactionPage('test_findTransactionByID'))
    return suite


if __name__ == '__main__':
    runner = unittest.TextTestRunner()
    runner.run(suite())