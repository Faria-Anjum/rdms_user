from playwright.sync_api import expect
import time, random

class FieldForcePage:
    def __init__(self, page):
        self.page = page
        self.url = "https://stage-dms.robi.com.bd/#/fieldforce/"

    def navigateToFieldForceApp(self):
        expect(self.page.get_by_text("Field Force App")).to_be_visible()
        self.page.get_by_text("Field Force App", exact=True).click()
        expect(self.page.get_by_role("link", name="Error Guide")).to_be_visible()
        expect(self.page.get_by_role("link", name="FAQ")).to_be_visible()
    
    def navigateToErrorGuide(self):
        self.page.get_by_role("link", name="Error Guide").click()
        expect(self.page).to_have_url(self.url+"error-guide")
        expect(self.page.get_by_role("main").get_by_text("Error Guide List")).to_be_visible()
    
    def navigateToFaq(self):
        self.page.get_by_role("link", name="FAQ").click()
        expect(self.page).to_have_url(self.url+"ffa-faq")

class ErrorGuidePage(FieldForcePage):
    def __init__(self, page, readErrorID):
        self.page = page
        self.url = "https://stage-dms.robi.com.bd/#/fieldforce/"
        self.ID = readErrorID
        self.error = "Automated test error - " + self.ID
        self.feature = "Error Guide"
        self.activation = 'Activation test error'

    def clickAddNewErrorGuide(self):
        expect(self.page.get_by_role("main").get_by_text(self.feature+" List", exact=True)).to_be_visible()
        url = self.page.url
        expect(self.page.get_by_role("link", name="Add New")).to_be_visible()
        self.page.get_by_role("link", name="Add New").click()
        expect(self.page).to_have_url(url+"/create")

    def createNewErrorGuide(self):
        expect(self.page.get_by_text("Create New Error Guide Item")).to_be_visible()
        self.page.get_by_placeholder("Enter error code").click()
        self.page.get_by_placeholder("Enter error code").fill(self.ID)
        self.page.get_by_placeholder("Provide details for this").click()
        self.page.get_by_placeholder("Provide details for this").fill(self.error)
        self.page.get_by_placeholder("Provide possible solution").click()
        self.page.get_by_placeholder("Provide possible solution").fill("test solution")
        self.page.get_by_placeholder("Enter sort order (number, e.g").click()
        self.page.get_by_placeholder("Enter sort order (number, e.g").fill("0")
        self.page.get_by_label("Platform *").select_option(str(random.randrange(1,3)))
        self.page.get_by_label("Status *").select_option("true")

    def clickSubmit(self):
        print(self.ID)
        self.page.get_by_role("button", name="Submit").click()

    def confirmNewErrorGuide(self):
        expect(self.page.get_by_text("Created Successfully")).to_be_visible()
        self.page.get_by_text("Created Successfully").click()
        expect(self.page.get_by_text(self.ID, exact = True)).to_be_visible()

    def updateErrorGuide(self):
        def writeErrorGuideID():
            with open(r"files\errorguide_id.txt",'r') as f:
                st = int(f.read())
            with open(r"files\errorguide_id.txt",'w') as f:
                nst = st + 1
                f.write(str(nst))
            return st
        writeErrorGuideID()

    def checkNumericErrorCode(self):
        self.page.get_by_placeholder("Enter error code").fill("avgv")
        expect(self.page.get_by_text("Invalid input")).to_be_visible()

    def checkNumericSortOrder(self):
        self.page.get_by_placeholder("Enter sort order (number, e.g").fill("a")
        expect(self.page.get_by_text("sortOrder must be a `number` type")).to_be_visible()
    
    def requiredFieldWarning(self):
        # field = self.page.get_by_text("Error Code Description *")
        # expect(field).to_be_visible()
        expect(self.page.get_by_text("This field is required", exact = True).first).to_be_visible()

    def editErrorGuide(self):
        row = self.page.locator(f"tr:has-text('{self.ID}')")
        expect(row).to_be_visible()
        row.get_by_role("link").click()
        expect(self.page.get_by_text("Update Error Guide Item")).to_be_visible()
        time.sleep(0.25)
        desc = self.page.get_by_placeholder("Provide details for this").input_value()
        self.page.get_by_placeholder("Provide details for this").fill(desc+' - edited')

    def confirmEditedErrorGuide(self):
        # expect(self.page.get_by_text("Updated Successfully")).to_be_visible()
        row = self.page.locator(f"tr:has-text('{self.ID}')")
        expect(row.locator("td:nth-child(2)")).to_contain_text("edited")

    def toggleErrorGuideActivation(self):
        row = self.page.locator(f"tr:has-text('{self.activation}')")
        expect(row.get_by_role("button")).to_be_visible()
        row.get_by_role("button").click()
        self.page.get_by_text("Status Changed").click()

    def checkInactivatedErrorGuide(self):
        self.page.get_by_text("Inactive", exact=True).click()
        row = self.page.locator(f"tr:has-text('{self.activation}')")
        expect(row).to_be_visible()

    def checkActivatedErrorGuide(self):
        self.page.get_by_text("Active", exact=True).click()
        row = self.page.locator(f"tr:has-text('{self.activation}')")
        expect(row).to_be_visible()

class FAQPage(ErrorGuidePage):
    def __init__(self, page, readFAQID):
        self.page = page
        self.url = "https://stage-dms.robi.com.bd/#/fieldforce/"
        self.ID = f" Automated test question [{readFAQID}"
        self.feature = "FAQ"

    def clickAddNewFAQ(self):
        return super().clickAddNewErrorGuide()
    
    def createNewFAQ(self, type):
        global name
        platforms = ["RDMS", "SFA", "RedCube"]
        platform = random.choice(platforms)
        name = platform+self.ID+'-'+type.lower()+']'
        expect(self.page.get_by_text("Create New FAQ")).to_be_visible()
        self.page.get_by_placeholder("Type your question..").click()
        self.page.get_by_placeholder("Type your question..").fill(name)
        self.page.get_by_label("Platform *").select_option(platform)
        self.page.get_by_placeholder("Enter sort order (number, e.g").click()
        self.page.get_by_placeholder("Enter sort order (number, e.g").fill("0")

    def basicFAQAnswer(self):
        self.page.get_by_label("FAQ Type *").select_option('BASIC')
        self.page.get_by_placeholder("Provide answer to your").click()
        self.page.get_by_placeholder("Provide answer to your").fill("test answer")

    def pictureFAQAnswer(self):
        self.page.get_by_label("FAQ Type *").select_option('PICTURE')
        with self.page.expect_file_chooser() as fc_info:
            self.page.get_by_placeholder("Provide an image file").click()
            file_chooser = fc_info.value
            file_chooser.set_files(r"files\rdms_logo.png")

    def videoFAQAnswer(self):
        self.page.get_by_label("FAQ Type *").select_option('VIDEO')
        self.page.get_by_placeholder("Provide a youtube video link").click()
        self.page.get_by_placeholder("Provide a youtube video link").fill("https://youtu.be/rmC5bLymUgs?si=Q8wSP7NiPHd72o-H")

    def confirmNewFAQ(self):
        self.page.get_by_text("Created Successfully").click()
        expect(self.page.get_by_text((name), exact = True)).to_be_visible()
    
    def checkURL(self):
        self.page.get_by_label("FAQ Type *").select_option("VIDEO")
        self.page.get_by_placeholder("Provide a youtube video link").click()
        self.page.get_by_placeholder("Provide a youtube video link").fill("youtube")
        expect(self.page.get_by_text("Must be a valid URL")).to_be_visible()
        #self.page.pause()

    def updateFAQID(self):
        def writeFAQID():
            with open(r"files\faq_id.txt",'r') as f:
                st = int(f.read())
            with open(r"files\faq_id.txt",'w') as f:
                nst = st + 1
                f.write(str(nst))
            return st
        writeFAQID()

    def editFAQ(self):
        #row = self.page.locator(f"tr:has-text('{self.ID[:25]} {int(self.ID[26:])-1}')")
        row = self.page.locator(f"tr:has-text('{name}')")
        expect(row).to_be_visible()
        row.get_by_role("link").click()
        self.page.get_by_placeholder("Type your question..").click()
        self.page.get_by_placeholder("Type your question..").fill(f"{name}_edit")
        self.page.get_by_role("button", name="Update").click()

    def clickCancel(self):
        self.page.get_by_role("button", name="Cancel").click()
        expect(self.page.get_by_role("main").get_by_text("FAQ List")).to_be_visible()
        
    def confirmEditedFAQ(self):
        self.page.get_by_text("Created Successfully").click()
        row = self.page.locator(f"tr:has-text('{name}')")
        expect(row.locator("td:nth-child(2)")).to_contain_text(f"{name}_edit")

    def toggleFAQActivation(self):
        self.activation = name+'_edit'
        ErrorGuidePage.toggleErrorGuideActivation(self)

    def checkInactivatedFAQ(self):
        ErrorGuidePage.checkInactivatedErrorGuide(self)

    def checkActivatedFAQ(self):
        ErrorGuidePage.checkActivatedErrorGuide(self)