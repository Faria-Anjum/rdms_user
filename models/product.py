from playwright.sync_api import expect
import time, re
#Anjum@reddot01

class ProductListPage:
    def __init__(self, page):
        self.page = page
        self.url = "https://stage-dms.robi.com.bd/#/product/"

    def navigateToProductList(self):
        self.page.get_by_text("Product", exact=True).click()
        expect(self.page.get_by_role("link", name="Product List")).to_be_visible()
        self.page.get_by_role("link", name="Product List").click()
        expect(self.page).to_have_url(self.url+"list")
        expect(self.page.get_by_role("main").get_by_text("Product List")).to_be_visible()
    
    def navigateToProductAdd(self):
        expect(self.page.get_by_role("link", name="Product Add")).to_be_visible()
        self.page.get_by_role("link", name="Product Add").click()
        expect(self.page).to_have_url(self.url+"add")

class CreateProductPage(ProductListPage):
    def __init__(self, page, readProductID):
        self.page = page
        self.url = "https://stage-dms.robi.com.bd/#/product/"
        self.productNameL = "test_product_l_" + str(readProductID)
        self.productNameP = "test_product_p_" + str(readProductID)
        self.productID = readProductID

    def createLogicalProduct(self, today):
        self.page.get_by_placeholder("Enter Product Name").click()
        self.page.get_by_placeholder("Enter Product Name").fill(self.productNameL)

        self.page.get_by_placeholder("Enter Material Code").click()
        self.page.get_by_placeholder("Enter Material Code").fill(self.productID)
        
        self.page.get_by_label("Brand *").select_option("2")
        self.page.get_by_label("Product Category *").select_option("3006") #airtel easy load
        self.page.get_by_label("Product Type").select_option("1018")
        self.page.get_by_label("Product Sub-Type").select_option("1014")

        self.page.get_by_placeholder("Enter Distributor Lifting").click()
        self.page.get_by_placeholder("Enter Distributor Lifting").fill("30")
        self.page.get_by_placeholder("Enter Retail Price").click()
        self.page.get_by_placeholder("Enter Retail Price").fill("40")
        self.page.get_by_placeholder("Enter MRP Price").click()
        self.page.get_by_placeholder("Enter MRP Price").fill("50")

        self.page.get_by_placeholder("Enter Start Date").fill(today)
        expect(self.page.get_by_role("button", name="Submit")).to_be_visible()
        self.page.get_by_role("button", name="Submit").click()

    def createPhysicalProduct(self, today):
        self.page.get_by_placeholder("Enter Product Name").click()
        self.page.get_by_placeholder("Enter Product Name").fill(self.productNameP)

        self.page.get_by_placeholder("Enter Material Code").click()
        self.page.get_by_placeholder("Enter Material Code").fill(self.productID)

        self.page.get_by_label("Brand *").select_option("1")
        self.page.get_by_label("Product Category *").select_option("3010") #sim
        self.page.get_by_label("Product Type").select_option("1009")
        self.page.get_by_label("Product Sub-Type").select_option("1010")

        self.page.get_by_placeholder("Enter Distributor Lifting").click()
        self.page.get_by_placeholder("Enter Distributor Lifting").fill("250")
        self.page.get_by_placeholder("Enter Retail Price").click()
        self.page.get_by_placeholder("Enter Retail Price").fill("300")
        self.page.get_by_placeholder("Enter MRP Price").click()
        self.page.get_by_placeholder("Enter MRP Price").fill("350")

        self.page.get_by_placeholder("Enter Start Date").fill(today)
        expect(self.page.get_by_role("button", name="Submit")).to_be_visible()
        self.page.get_by_role("button", name="Submit").click()

    def confirmCreatedProduct(self):
        def writeProductID():
            with open(r"files\product_id.txt",'r') as f:
                st = int(f.read())
            with open(r"files\product_id.txt",'w') as f:
                nst = st + 1
                f.write(str(nst))
            return st
        expect(self.page.get_by_text("Created Successfully...")).to_be_visible()
        self.page.get_by_role("button", name="Close").click()
        expect(self.page.get_by_role("main").get_by_text("Product List")).to_be_visible()
        writeProductID()

    def findCreatedProduct(self):
        expect(self.page.locator("tr:nth-child(2) td:first-child")).to_contain_text(self.productID)

class ValidationChecks(ProductListPage):
    def checkUniqueMaterialCode(self):
        time.sleep(0.25)
        self.page.get_by_placeholder("Enter Material Code").click()
        self.page.get_by_placeholder("Enter Material Code").fill("4001")
        expect(self.page.get_by_text("This Material Code already")).to_be_visible()

    def checkNegetivePrice(self):
        self.page.get_by_placeholder("Enter Distributor Lifting").click()
        self.page.get_by_placeholder("Enter Distributor Lifting").fill("-8")
        expect(self.page.get_by_text("Give a valid price value")).to_be_visible()
        self.page.get_by_placeholder("Enter Retail Price").click()
        self.page.get_by_placeholder("Enter Retail Price").fill("-6")
        expect(self.page.get_by_text("Give a valid price value").nth(1)).to_be_visible()
        self.page.get_by_placeholder("Enter MRP Price").click()
        self.page.get_by_placeholder("Enter MRP Price").fill("-1")
        expect(self.page.get_by_text("Give a valid price value").nth(2)).to_be_visible()

    def checkTypeSequence(self):
        expect(self.page.get_by_label("Product Type *")).to_contain_text("Select Product Category First")
        # page.get_by_label("Product Category *").select_option("3006")
        # expect(page.get_by_label("Product Type")).to_contain_text("Select Product Type Airtel Easy Load")
        self.page.get_by_label("Product Category *").select_option("3010")
        expect(self.page.get_by_label("Product Type")).to_contain_text("Select Product Type ReplacementSIMMNP_Replacement")

    def checkDateSequence(self):
        endDateDiv = self.page.locator("div").filter(has_text=re.compile(r"^End Date$")).first
        expect(endDateDiv.get_by_placeholder("Select Start date first")).to_be_disabled()
        self.page.get_by_placeholder("Enter Start Date").fill("2024-11-20")
        expect(endDateDiv.get_by_placeholder("Select Start date first")).to_be_enabled()

    def checkDateValidation(self):
        self.page.get_by_placeholder("Select Start date first").fill("2024-11-01")
        expect(self.page.get_by_text("End date must be after Start")).to_be_visible()
        self.page.get_by_placeholder("Select Start date first").fill("")

    def clickCancel(self):
        self.page.get_by_role("button", name="Cancel").click()
        expect(self.page.get_by_role("main").get_by_text("Product List")).to_be_visible()

class EditProductPage(ProductListPage):
    def navigateToProductEdit(self):
        row = self.page.locator("tr:nth-child(2)")
        row.get_by_role("link", name="").click()
        expect(self.page.get_by_text("View Product")).to_be_visible()
        self.page.get_by_role("button", name="Edit").click()
        expect(self.page.get_by_text("Update Product")).to_be_visible()

    def editProductInput(self):
        self.page.get_by_label("Brand *").select_option("2") #edit sim type as mnp replacement
        self.page.get_by_label("Product Type").select_option("1010")

    def clickUpdate(self):
        self.page.get_by_role("button", name="Update").click()
        
    def confirmEdit(self):
        expect(self.page.get_by_text("Updated Successfully...")).to_be_visible()
        self.page.get_by_role("button", name="Close").click()
        expect(self.page.get_by_role("main").get_by_text("Product List")).to_be_visible()
        row = self.page.locator("tr:nth-child(2)")
        expect(row.locator("td:nth-child(4)")).to_contain_text("MNP_Replacement") #type
        expect(row.locator("td:nth-child(5)")).to_contain_text("Airtel") #brand

    def confirmDateRestrictedActivation(self, tomorrow):
        self.page.get_by_placeholder("Enter Start Date").fill(tomorrow)
        self.page.get_by_role("button", name="Update").click()
        expect(self.page.get_by_text("Updated successfully...")).to_be_visible()
        self.page.get_by_text("Inactive", exact=True).click()
        row = self.page.locator("tr:nth-child(2)")
        expect(row.locator("td:first-child")).to_contain_text(CreateProductPage.productID)

    def inactivateProduct(self):
        self.page.get_by_role("cell", name="Code ").locator("span").click()
        self.page.get_by_role("textbox").click()
        self.page.get_by_role("textbox").fill("4001")
        self.page.get_by_role("button", name="Filter").click()
        row = self.page.locator("tr", has_text="4001")
        row.get_by_role("link", name="").click()
        self.page.get_by_role("button", name="Edit").click()
        self.page.get_by_label("Status *").select_option("false")
        self.page.get_by_role("button", name="Update").click()

    def checkInactivatedProduct(self):
        expect(self.page.get_by_text("Updated successfully...")).to_be_visible()
        self.page.get_by_text("Inactive", exact=True).click()
        self.page.get_by_role("cell", name="Code ").locator("i").click()
        self.page.get_by_role("textbox").click()
        self.page.get_by_role("textbox").fill("4001")
        self.page.get_by_role("button", name="Filter").click()
        expect(self.page.locator("tr:nth-child(2) td:first-child")).to_contain_text("4001")

    def activateProduct(self):
        row = self.page.locator("tr", has_text="4001")
        row.get_by_role("link", name="").click()
        self.page.get_by_role("button", name="Edit").click()
        self.page.get_by_label("Status *").select_option("true")
        self.page.get_by_role("button", name="Update").click()

    def checkActivatedProduct(self):
        expect(self.page.get_by_text("Updated successfully...")).to_be_visible()
        self.page.get_by_text("Active", exact=True).click()
        self.page.get_by_role("cell", name="Code ").locator("i").click()
        self.page.get_by_role("textbox").click()
        self.page.get_by_role("textbox").fill("4001")
        self.page.get_by_role("button", name="Filter").click()
        expect(self.page.locator("tr:nth-child(2) td:first-child")).to_contain_text("4001")