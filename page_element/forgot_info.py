class ForgotInfoElements:
    TXTBOX_FIRSTNAME = "//input[@id='firstName']"
    TXTBOX_LASTNAME = "//input[@id='lastName']"
    TXTBOX_STREET = "//input[@id='address.street']"
    TXTBOX_CITY = "//input[@id='address.city']"
    TXTBOX_STATE = "//input[@id='address.state']"
    TXTBOX_ZIPCODE = "//input[@id='address.zipCode']"
    TXTBOX_SSN = "//input[@id='ssn']"
    BTN_FINDINFO = "//input[@type ='submit' and @value='Find My Login Info']"
    TXT_USERNAMEPW = "//div[@id='rightPanel']//p[2]"
    
class ForgotErrorMsgElements:
    TXT_FIRSTNAME_ERROR = "//span[@id='firstName.errors']"
    TXT_LASTNAME_ERROR = "//span[@id='lastName.errors']"
    TXT_STREET_ERROR = "//span[@id='address.street.errors']"
    TXT_CITY_ERROR = "//span[@id='address.city.errors']"
    TXT_STATE_ERROR = "//span[@id='address.state.errors']"
    TXT_ZIPCODE_ERROR = "//span[@id='address.zipCode.errors']"
    TXT_SSN_ERROR = "//span[@id='ssn.errors']"