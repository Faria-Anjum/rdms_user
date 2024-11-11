from models.main import LoginPage, UserListPage, EditUserPage, CreateUserPage, InputValidityCheck
import pytest

def test_login(page):
    '''User can log in'''
    login = LoginPage(page)
    login.navigate()
    login.loginCreds()
    login.clickSignIn()
    login.confirmSignedIn()

def test_createUser(page, readUserIndx):
    '''User can navigate to Create User page and add user'''
    newuser = CreateUserPage(page, readUserIndx)
    newuser.navigateToUserList()
    newuser.navigateToUserAdd()
    newuser.createUser()
    newuser.confirmCreatedUser()
    newuser.findCreatedUser()

def test_invalidMobileNumber(page, readUserIndx):
    '''User receives error for invalid mobile number'''
    newuser = InputValidityCheck(page)
    p = CreateUserPage(page, readUserIndx)
    p.navigateToUserList()
    newuser.navigateToUserAdd()
    newuser.invalidMobileNumber()

def test_dropDownChoiceSequence(page):
    '''User cannot select drop down options unless in sequence'''
    newuser = InputValidityCheck(page)
    newuser.userAccessGroupSequence()
    newuser.areaChannelDistribSequence()

def test_clickAddCancel(page):
    cancelCheck = InputValidityCheck(page)
    cancelCheck.clickCancel()

def test_selectionReset(page):
    edituser = EditUserPage(page)
    edituser.navigateToUserEdit()
    edituser.checkUserSequence()
    edituser.checkLocationSequence()

def test_clickEditCancel(page):
    edituser = EditUserPage(page)
    edituser.editUserInput()
    edituser.clickCancel()
    edituser.checkCancel()

def test_disabledEnabledFields(page):
    edituser = EditUserPage(page)
    edituser.navigateToUserEdit()
    edituser.editUserDisabledField()
    edituser.editUserEnabledFields()

def test_updateUserInfo(page):
    edituser = EditUserPage(page)
    edituser.editUserInput()
    edituser.clickUpdate()
    edituser.confirmEdit()

def test_userInactivation(page, readUserIndx):
    activation = UserListPage(page, readUserIndx)
    activation.inactivateUser()
    activation.checkInactivatedUser()

def test_userActivation(page, readUserIndx):
    activation = UserListPage(page, readUserIndx)
    activation.activateUser()
    activation.checkActivatedUser()


