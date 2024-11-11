from playwright.sync_api import expect
import time
#Anjum@reddot01

class LoginPage:
    def __init__(self, page):
        self.page = page
        self.url = "https://stage-dms.robi.com.bd/"

    def navigate(self):
        self.page.goto(self.url, wait_until="load")
        expect(self.page).to_have_url(self.url+"#/login")
        expect(self.page.get_by_role("link", name="Robi").first).to_be_visible()
    
    def loginCreds(self):
        expect(self.page.get_by_role("heading", name="Login to Your Account")).to_be_visible()

        expect(self.page.get_by_placeholder("Enter User ID")).to_be_visible()
        self.page.get_by_placeholder("Enter User ID").click()
        self.page.get_by_placeholder("Enter User ID").fill("f.anjum")
        
        expect(self.page.get_by_placeholder("Password")).to_be_visible()
        self.page.get_by_placeholder("Password").click()
        self.page.get_by_placeholder("Password").fill("Anjum@reddot01")
        
    def clickSignIn(self):
        expect(self.page.get_by_role("button", name="Sign In")).to_be_visible()
        self.page.get_by_role("button", name="Sign In").click()

    def confirmSignedIn(self):
        expect(self.page.get_by_text("Signed In Successfully.")).to_be_visible()
        self.page.get_by_label("close").click()
        expect(self.page.get_by_text("Welcome")).to_be_visible()
        expect(self.page.get_by_role("link", name="Dashboard")).to_be_visible()

class UserListPage:
    def __init__(self, page, readUserIndx):
        self.page = page
        self.url = "https://stage-dms.robi.com.bd/#/user/"
        self.userID = "au." + str(readUserIndx-1)

    def navigateToUserList(self):
        self.page.get_by_text("Users & Roles").click()
        expect(self.page.get_by_role("link", name="User List")).to_be_visible()
        self.page.get_by_role("link", name="User List").click()
        expect(self.page).to_have_url(self.url+"list")
        expect(self.page.get_by_role("main").get_by_text("User List")).to_be_visible()
    
    def navigateToUserAdd(self):
        expect(self.page.get_by_role("link", name="User Add")).to_be_visible()
        self.page.get_by_role("link", name="User Add").click()
        time.sleep(0.25)
        expect(self.page).to_have_url(self.url+"add")

    def inactivateUser(self):
        self.page.get_by_role("cell", name="User ID ").locator("i").click()
        self.page.get_by_role("textbox").click()
        self.page.get_by_role("textbox").fill("au.0")
        self.page.get_by_role("button", name="Filter").click()
        row = self.page.locator("tr", has_text="au.0")
        row.locator("div").click()
        self.page.get_by_role("button", name="Change Status").click()

    def checkInactivatedUser(self):
        expect(self.page.get_by_text("Successfully Inactivated...")).to_be_visible()
        self.page.get_by_text("Successfully Inactivated...").click()
        self.page.get_by_text("Inactive", exact=True).click()
        self.page.get_by_role("cell", name="User ID ").locator("i").click()
        self.page.get_by_role("textbox").click()
        self.page.get_by_role("textbox").fill("au.0")
        self.page.get_by_role("button", name="Filter").click()
        expect(self.page.locator("tr:nth-child(2) td:first-child")).to_contain_text("au.0")

    def activateUser(self):
        self.page.get_by_text("Inactive", exact=True).click()
        self.page.get_by_role("cell", name="User ID ").locator("i").click()
        self.page.get_by_role("textbox").click()
        self.page.get_by_role("textbox").fill("au.0")
        self.page.get_by_role("button", name="Filter").click()
        row = self.page.locator("tr", has_text="au.0")
        row.locator("div").click()
        self.page.get_by_role("button", name="Change Status").click()

    def checkActivatedUser(self):
        expect(self.page.get_by_text("Successfully Activated...")).to_be_visible()
        self.page.get_by_text("Successfully Activated...").click()
        self.page.get_by_text("Active", exact=True).click()
        self.page.get_by_role("cell", name="User ID ").locator("i").click()
        self.page.get_by_role("textbox").click()
        self.page.get_by_role("textbox").fill("au.0")
        self.page.get_by_role("button", name="Filter").click()
        expect(self.page.locator("tr:nth-child(2) td:first-child")).to_contain_text("au.0")
        
    def findCreatedUser(self):
        expect(self.page.locator("tr:nth-child(2) td:first-child")).to_contain_text(self.userID)

class CreateUserPage(UserListPage):
    def __init__(self, page, readUserIndx):
        self.page = page
        self.url = "https://stage-dms.robi.com.bd/#/user/"
        self.userID = "au." + str(readUserIndx)
        self.userName = "AutomatedUser" + str(readUserIndx)

    def createUser(self):
        self.page.get_by_placeholder("Enter User ID").click()
        self.page.get_by_placeholder("Enter User ID").fill(self.userID)

        self.page.get_by_placeholder("Enter User Name").click()
        self.page.get_by_placeholder("Enter User Name").fill(self.userName)
        self.page.get_by_placeholder("Enter User Contact Number").click()
        self.page.get_by_placeholder("Enter User Contact Number").fill("01800000000")

        self.page.get_by_placeholder("Enter User E-mail").click()
        self.page.get_by_placeholder("Enter User E-mail").fill("au@autest.com")

        self.page.get_by_label("User Type *").select_option("8")
        self.page.get_by_label("Access Group *").select_option("1")
        self.page.get_by_label("Authentication Type *").select_option("RDMS Authentication")

        self.page.get_by_label("Channel *").select_option("1011")
        self.page.get_by_label("Brand *").select_option("3")
        self.page.get_by_label("National").select_option("10366075")

        self.page.get_by_role("button", name="Submit").click()

    def confirmCreatedUser(self):
        def readWriteUserIndx():
            with open(r"files\username_index.txt",'r') as f:
                st = int(f.read())
            with open(r"files\username_index.txt",'w') as f:
                nst = st + 1
                f.write(str(nst))
            return st
        expect(self.page.get_by_text("Created Successfully...")).to_be_visible()
        readWriteUserIndx()
        self.page.get_by_role("button", name="Close").click()
        expect(self.page.get_by_role("main").get_by_text("User List")).to_be_visible()

    def clickCancel(self):
        self.page.get_by_role("button", name="Cancel").click()
        expect(self.page.get_by_role("main").get_by_text("User List")).to_be_visible()
        # self.page.get_by_role("cell", name="User ID ").locator("i").click()
        # self.page.get_by_role("textbox").click()
        # self.page.get_by_role("textbox").fill("au."+readUserIndx)
        # self.page.get_by_role("button", name="Filter").click()

class InputValidityCheck(CreateUserPage):
    def __init__(self, page):
        self.page = page
        self.url = "https://stage-dms.robi.com.bd/#/user/"

    def invalidMobileNumber(self):
        time.sleep(0.25)
        self.page.get_by_placeholder("Enter User Contact Number").click()
        self.page.get_by_placeholder("Enter User Contact Number").fill("0156u78678")
        expect(self.page.get_by_text("Invalid contact number(length must be 11 digits)")).to_be_visible()

    def userAccessGroupSequence(self):
        expect(self.page.get_by_label("Access Group *")).to_be_visible()
        expect(self.page.get_by_label("Access Group *")).to_contain_text("Select User Type First")
        self.page.get_by_label("User Type *").select_option("8")
        expect(self.page.get_by_label("Access Group *")).to_contain_text("Select Access Group Area ManagerRetailer - Approve by AM")

    def areaChannelDistribSequence(self):
        expect(self.page.get_by_label("National")).to_have_value("")
        expect(self.page.get_by_label("Cluster")).to_contain_text("Select Cluster")
        expect(self.page.get_by_label("Region")).to_contain_text("Select Region")
        expect(self.page.get_by_label("Area")).to_contain_text("Select Area")
        expect(self.page.get_by_label("Territory")).to_contain_text("Select Territory")
        
        self.page.get_by_label("National").select_option("10366075")
        self.page.get_by_text("...", exact=True).click()
        expect(self.page.get_by_text("Sorry, You have to select")).to_be_visible()
        self.page.get_by_role("button", name="Close").click()

        self.page.get_by_label("Channel *").select_option("1011")
        self.page.get_by_text("...", exact=True).click()
        self.page.get_by_role("button", name="Close").click()

        expect(self.page.get_by_label("Cluster")).not_to_contain_text("Select Cluster")
        self.page.get_by_label("Cluster").select_option("19492")
        expect(self.page.get_by_label("Region")).not_to_contain_text("Select Region")
        self.page.get_by_label("Region").select_option("19500")
        expect(self.page.get_by_label("Area")).not_to_contain_text("Select Area")
        self.page.get_by_label("Area").select_option("20860")
        expect(self.page.get_by_label("Territory")).not_to_contain_text("Select Area")

class EditUserPage:
    def __init__(self, page):
        self.page = page
        self.url = "https://stage-dms.robi.com.bd/#/user/"

    def navigateToUserEdit(self):
        row = self.page.locator("tr:nth-child(2)")
        row.get_by_role("link", name="").click()
        expect(self.page.get_by_text("View User")).to_be_visible()
        self.page.get_by_role("button", name="Edit").click()
        expect(self.page.get_by_text("Update User")).to_be_visible()

    def checkUserSequence(self):
        self.page.get_by_label("User Type *").select_option("")
        expect(self.page.get_by_label("Access Group")).to_have_value("")

    def checkLocationSequence(self):
        self.page.get_by_label("Cluster").select_option("19493")
        self.page.get_by_label("National").select_option("")
        expect(self.page.get_by_label("Cluster")).to_have_value("")
        expect(self.page.get_by_label("Region")).to_have_value("")
        expect(self.page.get_by_label("Area")).to_have_value("")
        expect(self.page.get_by_label("Territory")).to_have_value("")

    def editUserDisabledField(self):
        expect(self.page.get_by_placeholder("Enter User User ID")).to_be_disabled()

    def editUserEnabledFields(self):
        expect(self.page.get_by_placeholder("Enter User Name")).to_be_enabled()
        expect(self.page.get_by_label("User Type *")).to_be_enabled()
        expect(self.page.get_by_label("Access Group *")).to_be_enabled()
        expect(self.page.get_by_label("Brand *")).to_be_enabled()
        expect(self.page.get_by_label("Cluster")).to_be_enabled()
        expect(self.page.get_by_label("Region")).to_be_enabled()
        expect(self.page.get_by_label("Area")).to_be_enabled()
        expect(self.page.get_by_label("Territory")).to_be_enabled()

    def editUserInput(self):
        self.page.get_by_placeholder("Enter User Name").click()
        self.page.get_by_placeholder("Enter User Name").fill("AutomatedUserEdit")
        self.page.get_by_label("User Type *").select_option("7")
        self.page.get_by_label("Access Group *").select_option("2")
        self.page.get_by_label("Brand *").select_option("2")
        self.page.get_by_label("National").select_option("10366075")

    def clickUpdate(self):
        self.page.get_by_role("button", name="Update").click()
        
    def confirmEdit(self):
        expect(self.page.get_by_text("Updated Successfully...")).to_be_visible()
        self.page.get_by_role("button", name="Close").click()
        expect(self.page.get_by_role("main").get_by_text("User List")).to_be_visible()
        row = self.page.locator("tr:nth-child(2)")
        expect(row.locator("td:nth-child(4)")).to_contain_text("RMG")
        expect(row.locator("td:nth-child(6)")).to_contain_text("Airtel")

    def clickCancel(self):
        self.page.get_by_role("button", name="Cancel").click()

    def checkCancel(self):
        expect(self.page.get_by_role("main").get_by_text("User List")).to_be_visible()
        row = self.page.locator("tr:nth-child(2)")
        expect(row.locator("td:nth-child(3)")).to_contain_text("AM")
        expect(row.locator("td:nth-child(6)")).to_contain_text("Both")