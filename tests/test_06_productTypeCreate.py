from models.productconfig import CreateProductTypeLogical, CreateProductTypePhysical, TypeValidationCheck, EditProductTypePage
from tests.test_01_authentication import test_validLogin as login

def test_login(page):
    login(page)

def test_createLogicalProductType(page, readProductTypeCode):
    '''User can navigate to Create Product Type page and add logical product type'''
    newproducttype = CreateProductTypeLogical(page, readProductTypeCode)
    newproducttype.navigateToProductTypeList()
    newproducttype.navigateToProductTypeAdd()
    newproducttype.createProductType()
    newproducttype.confirmCreatedProductType()
    newproducttype.findCreatedProduct()

def test_createPhysicalProductType(page, readProductTypeCode):
    '''User can navigate to Create Product Type page and add physical product type'''
    newproducttype = CreateProductTypePhysical(page, readProductTypeCode)
    newproducttype.navigateToProductTypeAdd()
    newproducttype.createProductType()
    newproducttype.confirmCreatedProductType()
    newproducttype.findCreatedProduct()

def test_inputValidation(page):
    validation = TypeValidationCheck(page)
    validation.navigateToProductTypeAdd()
    validation.checkUniqueProductTypeCode()
    validation.clickCancel()

def test_editProductType(page):
    editproduct = EditProductTypePage(page)
    editproduct.navigateToTypeEdit()
    editproduct.editProductInput()
    editproduct.clickUpdate()
    editproduct.confirmEdit()