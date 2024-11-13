from models.authentication import LoginPage, InactiveLogin, InvalidLogin, ForgotPassword

def test_invalidUsername(page):
    '''User can't log in with invalid username'''
    login = InvalidLogin(page)
    login.navigate()
    login.loginUser()
    login.loginPass()
    login.clickSignIn()
    login.confirmInvalid()

def test_invalidPassword(page):
    '''User can't log in with invalid password'''
    login = LoginPage(page)
    login.loginUser()
    login.incorrectPass()
    login.clickSignIn()
    login.confirmInvalidPass()

def test_inactiveLogin(page):
    login = InactiveLogin(page)
    login.loginUser()
    login.loginPass()
    login.clickSignIn()
    login.confirmInactive()

def test_forgotPassword(page):
    password = ForgotPassword(page)
    password.clickForgotPassword()

def test_passResetInvalidUsername(page):
    password = ForgotPassword(page)
    password.passResetInvalidUser()
    password.passResetValidMobile()
    password.clickSendOtp()
    password.userNotFound()

def test_passResetInvalidMobile(page):
    password = ForgotPassword(page)
    password.passResetValidUser()
    password.passResetInvalidMobile()

def test_passResetValidCreds(page):
    password = ForgotPassword(page)
    password.passResetValidUser()
    password.passResetValidMobile()
    password.clickSendOtp()
    password.enterOtp()

def test_wrongOTP(page):
    password = ForgotPassword(page)
    password.wrongOtp()

def test_clickBack(page):
    password = ForgotPassword(page)
    password.clickBack()

def test_validLogin(page):
    '''User can log in'''
    login = LoginPage(page)
    login.navigate()
    login.loginUser()
    login.loginPass()
    login.clickSignIn()
    login.confirmSignedIn()
    