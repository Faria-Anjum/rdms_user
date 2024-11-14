from playwright.sync_api import expect
from models.authentication import LoginPage

class AccessGroupNMG(LoginPage):
    def __init__(self, page):
        self.page = page
        self.url = "https://stage-dms.robi.com.bd/"
        self.username = "f.anjum"
        self.password = "Anjum@reddot01"

    def logout(self):
        self.page.get_by_text("Faria", exact=True).click()
        self.page.get_by_role("link", name="Sign Out").click()
        expect(self.page.get_by_text("Signed Out")).to_be_visible()
        self.page.get_by_text("Signed Out").click()

class AccessGroupAM(AccessGroupNMG):
    def __init__(self, page):
        self.page = page
        self.url = "https://stage-dms.robi.com.bd/"
        self.username = "faria"
        self.password = "Anjum@reddot03"

class SimActivationReportPage:
    def __init__(self, page):
        self.page = page
        self.url = "https://stage-dms.robi.com.bd/#/report/sim-activation"
    
    def simActivationReportVisible(self):
        self.page.get_by_text("Reports", exact=True).click()
        expect(self.page.get_by_role("link", name="Sim Activation Report")).to_be_visible()
        self.page.get_by_role("link", name="Sim Activation Report").click()
        expect(self.page).to_have_url(self.url)
        expect(self.page.get_by_role("main").get_by_text("Sim Activation Report")).to_be_visible()

    def simActivationReportNotVisible(self):
        self.page.get_by_text("Reports", exact=True).click()
        expect(self.page.get_by_role("link", name="Sim Activation Report")).not_to_be_visible()

class AccessGroupPage:
    def __init__(self, page):
        self.page = page
        self.url = "https://stage-dms.robi.com.bd/#/user/accessgroup/list"
        self.loginurl = "https://stage-dms.robi.com.bd/#/login"
    
    def navigateToUserAccessGroup(self):
        self.page.get_by_text("Users & Roles").click()
        self.page.get_by_role("link", name="Access Group List").click()
        expect(self.page).to_have_url(self.url)

    def editAMReportPermission(self):
        self.page.get_by_role("row", name="Area Manager AM ").get_by_role("link").click()
        self.page.get_by_role("button", name="Edit").click()
        self.page.get_by_role("main").get_by_text("Reports", exact=True).click()

    def removeAmSimActivationReportPermission(self):
        self.page.get_by_label("Sim Activation Report").uncheck()
        self.page.get_by_role("button", name="Update").click()
        expect(self.page.get_by_text("Updated Successfully...")).to_be_visible()
        self.page.get_by_text("Updated Successfully...").click()

    def giveAmSimActivationReportPermission(self):
        self.page.get_by_label("Sim Activation Report").check()
        self.page.get_by_role("button", name="Update").click()
        expect(self.page.get_by_text("Updated Successfully...")).to_be_visible()
        self.page.get_by_text("Updated Successfully...").click()