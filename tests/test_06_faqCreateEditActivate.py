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

def test_inputValidationUrlSortOrder(page, readFAQID):
    newfaq = FAQPage(page, readFAQID)
    newfaq.checkURL()
    newfaq.checkNumericSortOrder()
    newfaq.clickCancel()

def test_createVideoFAQ(page, readFAQID):
    newfaq = FAQPage(page, readFAQID)
    newfaq.clickAddNewFAQ()
    newfaq.createNewFAQ('VIDEO')
    newfaq.videoFAQAnswer()
    newfaq.clickSubmit()
    newfaq.confirmNewFAQ()

def test_createPictureFAQ(page, readFAQID):
    newfaq = FAQPage(page, readFAQID)
    newfaq.clickAddNewFAQ()
    newfaq.createNewFAQ('PICTURE')
    newfaq.pictureFAQAnswer()
    newfaq.clickSubmit()
    newfaq.confirmNewFAQ()

def test_createBasicFAQ(page, readFAQID):
    newfaq = FAQPage(page, readFAQID)
    newfaq.clickAddNewFAQ()
    newfaq.createNewFAQ('BASIC')
    newfaq.basicFAQAnswer()
    newfaq.clickSubmit()
    newfaq.confirmNewFAQ()
    newfaq.updateFAQID()

def test_editFAQ(page, readFAQID):
    newfaq = FAQPage(page, readFAQID)
    newfaq.editFAQ()
    newfaq.confirmEditedFAQ()

def test_FaqInactivation(page, readFAQID):
    newfaq = FAQPage(page, readFAQID)
    newfaq.toggleFAQActivation()
    newfaq.checkInactivatedFAQ()

def test_FaqActivation(page, readFAQID):
    newfaq = FAQPage(page, readFAQID)
    newfaq.toggleFAQActivation()
    newfaq.checkActivatedFAQ()