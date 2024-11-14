from models.productconfig import CreateNewCategoryLogical, CreateNewCategoryPhysical, CategoryValidationCheck
from tests.test_01_authentication import test_validLogin as login

def test_login(page):
    login(page)

def test_createLogicalCategory(page, readCategoryCode):
    '''User can navigate to Create Category page and add logical Category'''
    newcategory = CreateNewCategoryLogical(page, readCategoryCode)
    newcategory.navigateToProductTypeList()
    newcategory.navigateToProductTypeAdd()
    newcategory.createNewCategory()
    newcategory.confirmCreatedCategory()
    newcategory.findCreatedProduct()

def test_createPhysicalCategory(page, readCategoryCode):
    '''User can navigate to Create Category page and add physical Category'''
    newcategory = CreateNewCategoryPhysical(page, readCategoryCode)
    newcategory.navigateToProductTypeAdd()
    newcategory.createNewCategory()
    newcategory.confirmCreatedCategory()
    newcategory.findCreatedProduct()

def test_inputValidation(page):
    validation = CategoryValidationCheck(page)
    validation.navigateToProductTypeAdd()
    validation.checkUniqueCategoryName()
    validation.clickCancel()