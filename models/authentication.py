from playwright.sync_api import expect

class LoginPage:
    def __init__(self, page):
        self.page = page
        self.url = "https://stage-dms.robi.com.bd/"
        self.username = "f.anjum"
        self.password = "Anjum@reddot01"

    def navigate(self):
        self.page.goto(self.url, wait_until="load")
        expect(self.page).to_have_url(self.url+"#/login")
        expect(self.page.get_by_role("link", name="Robi").first).to_be_visible()
    
    def loginUser(self):
        expect(self.page.get_by_role("heading", name="Login to Your Account")).to_be_visible()

        expect(self.page.get_by_placeholder("Enter User ID")).to_be_visible()
        self.page.get_by_placeholder("Enter User ID").click()
        self.page.get_by_placeholder("Enter User ID").fill(self.username)
        
    def loginPass(self):
        expect(self.page.get_by_placeholder("Password")).to_be_visible()
        self.page.get_by_placeholder("Password").click()
        self.page.get_by_placeholder("Password").fill(self.password)

    def incorrectPass(self):
        expect(self.page.get_by_placeholder("Password")).to_be_visible()
        self.page.get_by_placeholder("Password").click()
        self.page.get_by_placeholder("Password").fill("abc")

    def confirmInvalidPass(self):
        expect(self.page.get_by_text("Bad credentials")).to_be_visible()
        
    def clickSignIn(self):
        expect(self.page.get_by_role("button", name="Sign In")).to_be_visible()
        self.page.get_by_role("button", name="Sign In").click()

    def confirmSignedIn(self):
        expect(self.page.get_by_text("Signed In Successfully.")).to_be_visible()
        self.page.get_by_label("close").click()
        expect(self.page.get_by_text("Welcome")).to_be_visible()
        expect(self.page.get_by_role("link", name="Dashboard")).to_be_visible()

class InactiveLogin(LoginPage):
    def __init__(self, page):
        self.page = page
        self.url = "https://stage-dms.robi.com.bd/"
        self.username = "inactive.user"
        self.password = "1active@Login"

    def confirmInactive(self):
        expect(self.page.get_by_text("User not found!")).to_be_visible()

class InvalidLogin(InactiveLogin):
    def __init__(self, page):
        self.page = page
        self.url = "https://stage-dms.robi.com.bd/"
        self.username = "anjum"
        self.password = "abc"

    def confirmInvalid(self):
        InactiveLogin.confirmInactive(self)

class ForgotPassword:
    def __init__(self, page):
        self.page = page
        self.url = "https://stage-dms.robi.com.bd/#/forgetpassword"
        self.username = "f.anjum"
        self.mobile = "1846888883"

    def clickForgotPassword(self):
        self.page.get_by_role("link", name="Forgot Password?").click()
        expect(self.page).to_have_url(self.url)

    def passResetValidUser(self):
        self.page.get_by_placeholder("Enter User ID").click()
        self.page.get_by_placeholder("Enter User ID").fill(self.username)

    def passResetInvalidUser(self):
        self.page.get_by_placeholder("Enter User ID").click()
        self.page.get_by_placeholder("Enter User ID").fill("abc")
    
    def passResetValidMobile(self):
        self.page.get_by_placeholder("Enter Mobile Number").click()
        self.page.get_by_placeholder("Enter Mobile Number").fill(self.mobile)

    def passResetInvalidMobile(self):
        self.page.get_by_placeholder("Enter Mobile Number").click()
        self.page.get_by_placeholder("Enter Mobile Number").fill("1476867545")
        expect(self.page.get_by_text("Mobile Number is not valid!")).to_be_visible()

    def clickSendOtp(self):
        expect(self.page.get_by_role("button", name=" Send OTP")).to_be_visible()
        self.page.get_by_role("button", name=" Send OTP").click()

    def userNotFound(self):
        expect(self.page.get_by_text("User Not Found", exact=True)).to_be_visible()

    def enterOtp(self):
        expect(self.page.get_by_text("OTP Number *")).to_be_visible()
        self.page.get_by_placeholder("Enter OTP Number").click()

    def wrongOtp(self):
        self.page.get_by_placeholder("Enter OTP Number").fill("5555")
        self.page.get_by_role("button", name=" Verify").click()
        expect(self.page.get_by_text("OTP doesn't match")).to_be_visible()
    
    def clickBack(self):
        self.page.get_by_role("link", name="Back").click()