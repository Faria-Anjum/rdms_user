from playwright.sync_api import expect
import time

class ProductTypeListPage:
    def __init__(self, page):
        self.page = page
        self.url = "https://stage-dms.robi.com.bd/#/product/type/"
        self.type = 'Type'

    def navigateToProductTypeList(self):
        self.page.get_by_text("Product Config", exact=True).click()
        expect(self.page.get_by_role("link", name=f"{self.type} List", exact=True)).to_be_visible()
        self.page.get_by_role("link", name=f"{self.type} List", exact=True).click()
        expect(self.page).to_have_url(self.url+'list')
        expect(self.page.get_by_role("main").get_by_text(f"Product {self.type} List")).to_be_visible()
    
    def navigateToProductTypeAdd(self):
        expect(self.page.get_by_role("link", name=f"{self.type} Add")).to_be_visible()
        self.page.get_by_role("link", name=f"{self.type} Add").click()
        expect(self.page).to_have_url(self.url+"add")

    def findCreatedProduct(self):
        expect(self.page.locator("tbody")).to_contain_text(self.name)

class ProductCategoryListPage(ProductTypeListPage):
    def __init__(self, page):
        self.page = page
        self.url = "https://stage-dms.robi.com.bd/#/product/category/"

class ProductSubTypeListPage(ProductTypeListPage):
    def __init__(self, page):
        self.page = page
        self.url = "https://stage-dms.robi.com.bd/#/product/subtype/"
        self.type = 'Sub Type'

    def navigateToProductSubTypeList(self):
        self.page.get_by_text("Product Config", exact=True).click()
        expect(self.page.get_by_role("link", name=f"{self.type} List", exact=True)).to_be_visible()
        self.page.get_by_role("link", name=f"{self.type} List", exact=True).click()
        expect(self.page).to_have_url(self.url+'list')
        expect(self.page.get_by_role("main").get_by_text(f"Product Sub-Type List")).to_be_visible()

class CreateProductTypeLogical(ProductTypeListPage):
    def __init__(self, page, readProductTypeCode):
        self.page = page
        self.url = "https://stage-dms.robi.com.bd/#/product/type/"
        self.name = "test_el_" + str(readProductTypeCode)
        self.productCode = "test-el-"+str(readProductTypeCode)
        self.category = "3006"
        self.type = 'Type'

    def createProductType(self):
        self.page.get_by_placeholder("Enter Product Type Name").click()
        self.page.get_by_placeholder("Enter Product Type Name").fill(self.productTypeName)
        self.page.get_by_placeholder("Enter Product Type Code").click()
        self.page.get_by_placeholder("Enter Product Type Code").fill(self.productCode)
        self.page.get_by_label("Product Category *").select_option(self.category) #airtel easy load
        self.page.get_by_role("button", name="Submit").click()

    def confirmCreatedProductType(self):
        def writeProductCode():
            with open(r"files\product_type.txt",'r') as f:
                st = int(f.read())
            with open(r"files\product_type.txt",'w') as f:
                nst = st + 1
                f.write(str(nst))
            return st
        
        expect(self.page.get_by_text("Created Successfully...")).to_be_visible()
        self.page.get_by_text("Created Successfully...").click()
        expect(self.page.get_by_role("main").get_by_text("Product Type List")).to_be_visible()
        writeProductCode()

class CreateProductTypePhysical(CreateProductTypeLogical):
    def __init__(self, page, readProductTypeCode):
        self.page = page
        self.url = "https://stage-dms.robi.com.bd/#/product/type/"
        self.productTypeName = "test_sim_" + str(readProductTypeCode)
        self.productCode = "test-sim-"+str(readProductTypeCode)
        self.category = "3010"
        self.type = 'Type'

class CreateNewCategoryLogical(ProductCategoryListPage):
    def __init__(self, page, readProductCategoryID):
        self.page = page
        self.url = "https://stage-dms.robi.com.bd/#/product/category/"
        self.name = "Test_Robi_EL_" + readProductCategoryID
        self.ioq = "EL"
        self.logical = "true"
        self.type = 'Category'

    def createNewCategory(self):
        self.page.get_by_placeholder("Enter Product Category Name").click()
        self.page.get_by_placeholder("Enter Product Category Name").fill(self.name)
        self.page.get_by_label("IOQ").select_option(self.ioq)
        self.page.get_by_label("Is Logical").select_option(self.logical)
        self.page.get_by_role("button", name="Submit").click()
        
    def confirmCreatedCategory(self):
        def writeCategoryCode():
            with open(r"files\product_category.txt",'r') as f:
                st = int(f.read())
            with open(r"files\product_category.txt",'w') as f:
                nst = st + 1
                f.write(str(nst))
            return st
        
        expect(self.page.get_by_text("Created Successfully...")).to_be_visible()
        self.page.get_by_text("Created Successfully...").click()
        expect(self.page.get_by_role("main").get_by_text("Product Category List")).to_be_visible()
        writeCategoryCode()

class CreateNewCategoryPhysical(ProductCategoryListPage):
    def __init__(self, page, readProductCategoryID):
        self.page = page
        self.url = "https://stage-dms.robi.com.bd/#/product/category/"
        self.name = "Test_Robi_SIM_" + readProductCategoryID
        self.ioq = "SIM"
        self.logical = "false"
        self.type = 'Category'

    def createNewCategory(self):
        self.page.get_by_placeholder("Enter Product Category Name").click()
        self.page.get_by_placeholder("Enter Product Category Name").fill(self.name)
        self.page.get_by_label("IOQ").select_option(self.ioq)
        self.page.get_by_label("Is Logical").select_option(self.logical)
        self.page.get_by_role("button", name="Submit").click()
        
    def confirmCreatedCategory(self):
        def writeCategoryCode():
            with open(r"files\product_category.txt",'r') as f:
                st = int(f.read())
            with open(r"files\product_category.txt",'w') as f:
                nst = st + 1
                f.write(str(nst))
            return st
        
        expect(self.page.get_by_text("Created Successfully...")).to_be_visible()
        self.page.get_by_text("Created Successfully...").click()
        expect(self.page.get_by_role("main").get_by_text("Product Category List")).to_be_visible()
        writeCategoryCode()

class CreateNewSubType(ProductSubTypeListPage):
    def __init__(self, page, readProductSubtypeID):
        self.page = page
        self.url = "https://stage-dms.robi.com.bd/#/product/subtype/"
        self.name = "Test_SubType_" + readProductSubtypeID
        self.type = 'Sub Type'

    def createNewSubType(self):
        self.page.get_by_placeholder("Enter Product Sub-Type Name").click()
        self.page.get_by_placeholder("Enter Product Sub-Type Name").fill(self.name)
        self.page.get_by_role("button", name="Submit").click()

    def confirmCreatedSubType(self):
        def writeSubTypeCode():
            with open(r"files\product_subtype.txt",'r') as f:
                st = int(f.read())
            with open(r"files\product_subtype.txt",'w') as f:
                nst = st + 1
                f.write(str(nst))
            return st
        
        expect(self.page.get_by_text("Created Successfully...")).to_be_visible()
        self.page.get_by_text("Created Successfully...").click()
        expect(self.page.get_by_role("main").get_by_text("Product Sub-Type List")).to_be_visible()
        writeSubTypeCode()

class TypeValidationCheck(ProductTypeListPage):
    def checkUniqueProductTypeCode(self):
        time.sleep(0.25)
        self.page.get_by_placeholder("Enter Product Type Code").click()
        self.page.get_by_placeholder("Enter Product Type Code").fill('EL01')
        expect(self.page.get_by_text("This code already exists")).to_be_visible()

    def clickCancel(self):
        self.page.get_by_role("button", name="Cancel").click()
        self.page.pause()
        expect(self.page.get_by_role("main").get_by_text("Product Type List")).to_be_visible()

class CategoryValidationCheck(ProductCategoryListPage):
    def __init__(self, page):
        self.page = page
        self.url = "https://stage-dms.robi.com.bd/#/product/category/"
        self.type = 'Category'

    def checkUniqueCategoryName(self):
        time.sleep(0.25)
        self.page.get_by_placeholder("Enter Product Category Name").click()
        self.page.get_by_placeholder("Enter Product Category Name").fill('Robi_Easy_Load')
        expect(self.page.get_by_text("This name already exists")).to_be_visible()

    def clickCancel(self):
        self.page.get_by_role("button", name="Cancel").click()
        expect(self.page.get_by_role("main").get_by_text("Product Category List")).to_be_visible()

class SubTypeValidationCheck(ProductCategoryListPage):
    def __init__(self, page):
        self.page = page
        self.url = "https://stage-dms.robi.com.bd/#/product/subtype/"
        self.type = 'Sub Type'

    def checkUniqueSubTypeName(self):
        time.sleep(0.25)
        self.page.get_by_placeholder("Enter Product Sub-Type Name").click()
        self.page.get_by_placeholder("Enter Product Sub-Type Name").fill('Both')
        expect(self.page.get_by_text("This name already exists")).to_be_visible()

    def clickCancel(self):
        self.page.get_by_role("button", name="Cancel").click()
        expect(self.page.get_by_role("main").get_by_text("Product Sub-Type List")).to_be_visible()

class EditProductTypePage(ProductTypeListPage):
    def __init__(self, page):
        self.page = page
        self.url = "https://stage-dms.robi.com.bd/#/product/type/"
        self.type = 'Type'
        self.col = 3

    def navigateToTypeEdit(self):
        row = self.page.locator("tr:nth-child(1)")
        row.get_by_role("link").click()
        expect(self.page.get_by_text(f"View Product {self.type}")).to_be_visible()
        self.page.get_by_role("button", name="Edit").click()
        expect(self.page.get_by_text(f"Update Product {self.type}")).to_be_visible()

    def editProductInput(self):
        self.page.get_by_placeholder(f"Enter Product {self.type} Description").fill(f"edited_test_{(self.type).lower()}")
        self.page.get_by_label("Status *").select_option("false")

    def clickUpdate(self):
        self.page.get_by_role("button", name="Update").click()
        
    def confirmEdit(self):
        expect(self.page.get_by_text("Updated Successfully...")).to_be_visible()
        self.page.get_by_role("button", name="Close").click()
        expect(self.page.get_by_role("main").get_by_text(f"Product {self.type} List")).to_be_visible()
        self.page.get_by_text("Inactive", exact=True).click()
        row = self.page.locator("tr:nth-child(1)")
        expect(row.locator(f"td:nth-child({self.col})")).to_contain_text(f"edited_test_{(self.type).lower()}") #description

    # page.get_by_text("Product Config").click()
    # page.get_by_role("link", name="Type List", exact=True).click()
    # page.get_by_text("Inactive", exact=True).click()
    # page.get_by_role("row", name="test_sim_7 SIM Inactive ").get_by_role("cell").nth(4).click()
    # page.get_by_role("row", name="test_sim_7 SIM Inactive ").get_by_role("link").click()
    # page.get_by_role("button", name="Edit").click()
    # page.get_by_placeholder("Enter Product Type Name").click()
    # page.get_by_placeholder("Enter Product Type Code").click()
    # page.get_by_placeholder("Enter Product Type Code").fill("t")
    # page.get_by_role("button", name="Cancel").click()
    # page.get_by_text("Inactive", exact=True).click()
    # page.get_by_role("row", name="test_sim_7 SIM Inactive ").get_by_role("link").click()
    # page.get_by_role("button", name="Edit").click()
    # page.get_by_label("Status *").select_option("true")
    # page.get_by_placeholder("Enter Product Type Name").click()
    # page.get_by_placeholder("Enter Product Type Name").fill("test_sim_7_edited")
    # page.get_by_role("button", name="Update").click()
    # page.get_by_role("group").get_by_text("Active", exact=True).click()
    # page.get_by_role("row", name="test_sim_7_edited SIM Active ").get_by_role("link").click()
    # page.get_by_role("button", name="Edit").click()
    # page.get_by_label("Status *").select_option("false")
    # page.get_by_role("button", name="Update").click()

class EditProductCategoryPage(EditProductTypePage):
    def __init__(self, page):
        self.page = page
        self.url = "https://stage-dms.robi.com.bd/#/product/category/"
        self.type = 'Category'
        self.col = 2

class EditProductSubTypePage(EditProductTypePage):
    def __init__(self, page):
        self.page = page
        self.url = "https://stage-dms.robi.com.bd/#/product/subtype/"
        self.type = 'Sub-Type'
        self.col = 2