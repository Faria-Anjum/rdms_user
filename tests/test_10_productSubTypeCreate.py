from models.productconfig import CreateNewSubType, SubTypeValidationCheck, EditProductSubTypePage
from tests.test_01_authentication import test_validLogin as login

def test_login(page):
    login(page)

def test_createSubType(page, readSubTypeCode):
    '''User can navigate to Create Sub Type page and add Sub Type'''
    newsubtype = CreateNewSubType(page, readSubTypeCode)
    newsubtype.navigateToProductSubTypeList()
    newsubtype.navigateToProductTypeAdd()
    newsubtype.createNewSubType()
    newsubtype.confirmCreatedSubType()
    newsubtype.findCreatedProduct()

def test_inputValidation(page):
    validation = SubTypeValidationCheck(page)
    validation.navigateToProductTypeAdd()
    validation.checkUniqueSubTypeName()
    validation.clickCancel()

def test_editProductSubType(page):
    editproduct = EditProductSubTypePage(page)
    editproduct.navigateToTypeEdit()
    editproduct.editProductInput()
    editproduct.clickUpdate()
    editproduct.confirmEdit()