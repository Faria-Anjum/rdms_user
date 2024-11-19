from models.product import CreateProductPage, EditProductPage, ValidationChecks
from tests.test_01_authentication import test_validLogin as login

def test_login(page):
    login(page)

def test_createLogicalProduct(page, readProductID, today):
    '''Product can navigate to Create Product page and add logical product'''
    newproduct = CreateProductPage(page, readProductID)
    newproduct.navigateToProductList()
    newproduct.navigateToProductAdd()
    newproduct.createLogicalProduct(today)
    newproduct.confirmCreatedProduct()
    newproduct.findCreatedProduct()

def test_createPhysicalProduct(page, readProductID, today):
    '''Product can navigate to Create Product page and add physical product'''
    newproduct = CreateProductPage(page, readProductID)
    newproduct.navigateToProductAdd()
    newproduct.createPhysicalProduct(today)
    newproduct.confirmCreatedProduct()
    newproduct.findCreatedProduct()

def test_inputValidation(page):
    validation = ValidationChecks(page)
    validation.navigateToProductAdd()
    validation.checkUniqueMaterialCode()

    validation.checkTypeSequence()
    validation.checkDateSequence()
    validation.checkDateValidation()
    
    validation.checkNegetivePrice()
    validation.clickCancel()

def test_updateProductInfo(page):
    editproduct = EditProductPage(page)
    editproduct.navigateToProductEdit()
    editproduct.editProductInput()
    editproduct.clickUpdate()
    editproduct.confirmEdit()

# def test_changeActivationThroughDate(page, tomorrow):
#     editproduct = EditProductPage(page)
#     editproduct.navigateToProductEdit()
#     editproduct.confirmDateRestrictedActivation(tomorrow)

def test_inactivateProduct(page):
    activation = EditProductPage(page)
    activation.inactivateProduct()
    activation.checkInactivatedProduct()

def test_activateProduct(page):
    activation = EditProductPage(page)
    activation.activateProduct()
    activation.checkActivatedProduct()