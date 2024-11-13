from models.user import EditUserPage, CreateUserPage
from tests.test_01_authentication import test_validLogin as login

def test_login(page):
    login(page)

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
    newuser = CreateUserPage(page, readUserIndx)
    newuser.navigateToUserAdd()
    newuser.invalidMobileNumber()

def test_dropDownChoiceSequence(page, readUserIndx):
    '''User cannot select drop down options unless in sequence'''
    newuser = CreateUserPage(page, readUserIndx)
    newuser.userAccessGroupSequence()
    newuser.areaChannelDistribSequence()
    newuser.clickCancel()

def test_editUser(page):
    edituser = EditUserPage(page)
    edituser.navigateToUserEdit()

def test_selectionReset(page):
    edituser = EditUserPage(page)
    edituser.checkUserSequence()
    edituser.checkLocationSequence()

def test_disabledEnabledFields(page):
    edituser = EditUserPage(page)
    edituser.editUserDisabledField()
    edituser.editUserEnabledFields()

def test_updateUserInfo(page):
    edituser = EditUserPage(page)
    edituser.editUserInput()
    edituser.clickUpdate()
    edituser.confirmEdit()

def test_userInactivation(page):
    activation = EditUserPage(page)
    activation.inactivateUser()
    activation.checkInactivatedUser()

def test_userActivation(page):
    activation = EditUserPage(page)
    activation.activateUser()
    activation.checkActivatedUser()


