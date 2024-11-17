from models.bulkuser import BulkUserCreatePage, BulkUserUpdatePage
from tests.test_01_authentication import test_validLogin as login

def test_login(page):
    login(page)

def test_createBulkUser(page, readBulkUserID):
    '''User can navigate to Create Bulk User page and select bulk file'''
    newbulkuser = BulkUserCreatePage(page, readBulkUserID)
    newbulkuser.navigateToUserListPage()
    newbulkuser.navigateToBulkUserCreate()

def test_uploadMissingColumnFile(page, readBulkUserID):
    '''File with missing column(s) cannot be uploaded'''
    newbulkuser = BulkUserCreatePage(page, readBulkUserID)
    newbulkuser.selectMissingColumnsFile()

def test_createValidBulkUserFile(page, readBulkUserID):
    newbulkuser = BulkUserCreatePage(page, readBulkUserID)
    newbulkuser.uploadValidFile()
    newbulkuser.confirmCreatedBulkUsers()

def test_updateBulkUser(page):
    '''User can go to to Update Bulk User page and select bulk file'''
    updatebulkuser = BulkUserUpdatePage(page)
    updatebulkuser.navigateToBulkUserUpdate()

def test_updateWithMissingColumnFile(page):
    '''File with missing column(s) cannot be uploaded'''
    updatebulkuser = BulkUserUpdatePage(page)
    updatebulkuser.createMissingColumnsFile()
    updatebulkuser.selectMissingColumnsFile()

def test_updateValidBulkUserFile(page):
    updatebulkuser = BulkUserUpdatePage(page)
    updatebulkuser.modifyValidBulkUsers()
    updatebulkuser.uploadValidFile()
    updatebulkuser.confirmUpdatedBulkUsers()