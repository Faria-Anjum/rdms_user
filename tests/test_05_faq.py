from models.fieldforceapp import FAQPage
from tests.test_01_authentication import test_validLogin as login

def test_login(page):
    login(page)

def test_faqRequiredFieldsWarning(page, readFAQID):
    newfaq = FAQPage(page, readFAQID)
    newfaq.navigateToFieldForceApp()
    newfaq.navigateToFaq()
    newfaq.clickAddNewFAQ()
    newfaq.clickSubmit()
    newfaq.requiredFieldWarning()

def test_createFAQ(page, readFAQID):
    '''Product can navigate to Create Product page and add logical product'''
    newfaq = FAQPage(page, readFAQID)
    newfaq.createNewFAQ()
    newfaq.clickSubmit()
    newfaq.confirmNewFAQ()
    newfaq.updateFAQID()

