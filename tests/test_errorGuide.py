from models.fieldforceapp import ErrorGuidePage
from tests.test_01_authentication import test_validLogin as login

def test_login(page):
    login(page)

def test_errorGuideRequiredFieldsWarning(page, readErrorID):
    newerrorguide = ErrorGuidePage(page, readErrorID)
    newerrorguide.navigateToFieldForceApp()
    newerrorguide.navigateToErrorGuide()
    newerrorguide.clickAddNewErrorGuide()
    newerrorguide.clickSubmit()
    newerrorguide.requiredFieldWarning()

def test_numericInputsOnlyAcceptNumeric(page, readErrorID):
    newerrorguide = ErrorGuidePage(page, readErrorID)
    newerrorguide.checkNumericErrorCode()
    newerrorguide.checkNumericSortOrder()

def test_createErrorGuide(page, readErrorID):
    '''Product can navigate to Create Product page and add logical product'''
    newerrorguide = ErrorGuidePage(page, readErrorID)
    newerrorguide.createNewErrorGuide()
    newerrorguide.clickSubmit()
    newerrorguide.confirmNewErrorGuide()
    newerrorguide.writeErrorGuide()

def test_editErrorGuide(page, readErrorID):
    newerrorguide = ErrorGuidePage(page, readErrorID)
    newerrorguide.editErrorGuide()
    newerrorguide.clickSubmit()
    newerrorguide.confirmEditedErrorGuide()
