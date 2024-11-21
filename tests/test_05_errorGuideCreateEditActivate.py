from models.fieldforceapp import ErrorGuidePage
from tests.test_01_authentication import test_validLogin as login

def test_login(page):
    login(page)
    #page.pause()

def test_errorGuideRequiredFieldsWarning(page, readErrorID):
    newerrorguide = ErrorGuidePage(page, readErrorID)
    newerrorguide.navigateToFieldForceApp()
    newerrorguide.navigateToErrorGuide()
    newerrorguide.clickAddNewErrorGuide()
    newerrorguide.clickSubmit()
    newerrorguide.requiredFieldWarning()

def test_numericInputsOnlyAcceptNumeric(page, readErrorID):
    newerrorguide = ErrorGuidePage(page, readErrorID)
    #newerrorguide.checkNumericErrorCode()
    newerrorguide.checkNumericSortOrder()

def test_createErrorGuide(page, readErrorID):
    newerrorguide = ErrorGuidePage(page, readErrorID)
    newerrorguide.createNewErrorGuide()
    newerrorguide.clickSubmit()
    newerrorguide.confirmNewErrorGuide()

def test_editErrorGuide(page, readErrorID):
    newerrorguide = ErrorGuidePage(page, readErrorID)
    newerrorguide.editErrorGuide()
    newerrorguide.clickSubmit()
    newerrorguide.confirmEditedErrorGuide()
    newerrorguide.updateErrorGuide()

def test_errorGuideInactivation(page, readErrorID):
    newerrorguide = ErrorGuidePage(page, readErrorID)
    newerrorguide.toggleErrorGuideActivation()
    newerrorguide.checkInactivatedErrorGuide()

def test_errorGuideActivation(page, readErrorID):
    newerrorguide = ErrorGuidePage(page, readErrorID)
    newerrorguide.toggleErrorGuideActivation()
    newerrorguide.checkActivatedErrorGuide()