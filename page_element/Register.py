class RegisterPageElements:
    # LINK_REGISTER = "//a[text()='Register']"
    TXTBOX_FIRSTNAME = "//input[@id='customer.firstName']"
    TXTBOX_LASTNAME = "//input[@id='customer.lastName']"
    TXTBOX_ADDRESS_STREET = "//input[@id='customer.address.street']"
    TXTBOX_ADDRESS_CITY = "//input[@id='customer.address.city']"
    TXTBOX_ADDRESS_STATE = "//input[@id='customer.address.state']"
    TXTBOX_ADDRESS_ZIPCODE = "//input[@id='customer.address.zipCode']"
    TXTBOX_PHONENUMBER = "//input[@id='customer.phoneNumber']"
    TXTBOX_SSN = "//input[@id='customer.ssn']"
    TXTBOX_USERNAME = "//input[@id='customer.username']"
    TXTBOX_PASSWORD = "//input[@id='customer.password']"
    TXTBOX_CONFIRMPW = "//input[@id='repeatedPassword']"
    BTN_REGISTER = "//input[@type ='submit' and @value='Register']"
    TXT_WELCOME = "//div[@id='rightPanel']/h1"
    TXT_CREATEDMSG = "//div[@id='rightPanel']/p"
    TXTBOX_USERNAMELOGIN = "//input[@name='username']"
    TXTBOX_PASSWORDLOGIN = "//input[@name='password']"
    BTN_LOGIN = "//input[@type ='submit' and @value='Log In']"
    TXT_WELCOMELOGIN = "//p[@class='smallText']"

class RegisterPageErrorMessage:
    TXT_FIRSTNAME_ERROR = "//span[@id='customer.firstName.errors']"
    TXT_LASTNAME_ERROR = "//span[@id='customer.lastName.errors']"
    TXT_STREET_ERROR = "//span[@id='customer.address.street.errors']"
    TXT_CITY_ERROR = "//span[@id='customer.address.city.errors']"
    TXT_STATE_ERROR = "//span[@id='customer.address.state.errors']"
    TXT_ZIPCODE_ERROR = "//span[@id='customer.address.zipCode.errors']"
    TXT_SSN_ERROR = "//span[@id='customer.ssn.errors']"
    TXT_USERNAME_ERROR = "//span[@id='customer.username.errors']"
    TXT_PASSWORD_ERROR = "//span[@id='customer.password.errors']"
    TXT_CONFIRMPW_ERROR = "//span[@id='repeatedPassword.errors']" 