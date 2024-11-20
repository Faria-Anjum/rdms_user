from playwright.sync_api import expect
import random

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
        self.error = "Automated test error - " + readErrorID
        self.feature = "Error Guide"

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
        self.page.get_by_label("Platform *").select_option(random.randrange(1,3))
        self.page.get_by_label("Status *").select_option("true")

    def clickSubmit(self):
        self.page.get_by_role("button", name="Submit").click()

    def confirmNewErrorGuide(self):
        expect(self.page.get_by_text("Created Successfully")).to_be_visible()
        self.page.get_by_text("Created Successfully").click()
        expect(self.page.get_by_text(self.ID, exact = True)).to_be_visible()

    def writeErrorGuide(self):
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
        desc = self.page.get_by_placeholder("Provide details for this").input_value()
        self.page.get_by_placeholder("Provide details for this").fill(desc+' - edited')

    def confirmEditedErrorGuide(self):
        # expect(self.page.get_by_text("Updated Successfully")).to_be_visible()
        row = self.page.locator(f"tr:has-text('{self.ID}')")
        expect(row.locator("td:nth-child(2)")).to_contain_text("edited")

    # def inactivateErrorGuide(self):
        


    #     self.page.get_by_role("link", name="Error Guide").click()
    #     self.page.get_by_text("Error Guide List").click()
    #     self.page.get_by_role("link", name="Add New").click()
    #     self.page.get_by_placeholder("Enter error code").click()
    #     self.page.get_by_placeholder("Enter error code").fill("1000")
    #     self.page.get_by_placeholder("Provide details for this").click()
    #     self.page.get_by_placeholder("Enter error code").click()
    #     self.page.get_by_placeholder("Enter error code").fill("avgv")
    #     self.page.get_by_placeholder("Provide details for this").click()
    #     self.page.get_by_text("Invalid input").click()
    #     self.page.get_by_placeholder("Enter error code").click()
    #     self.page.get_by_placeholder("Enter error code").fill("")
    #     self.page.get_by_role("button", name="Submit").click()
    #     self.page.get_by_role("row", name="abc test error RDMS 50 Active").get_by_role("link").click()
    #     self.page.get_by_placeholder("Enter error code").click()
    #     self.page.get_by_placeholder("Enter error code").fill("123")
    #     self.page.get_by_role("button", name="Submit").click()
    #     self.page.get_by_role("link", name="Add New").click()
    #     self.page.get_by_placeholder("Enter error code").click()
    #     self.page.get_by_placeholder("Enter error code").fill("1050")
    #     self.page.get_by_placeholder("Provide details for this").click()
    #     self.page.get_by_placeholder("Provide details for this").fill("test error3")
    #     self.page.get_by_placeholder("Provide possible solution").click()
    #     self.page.get_by_placeholder("Provide possible solution").fill("test solution")
    #     self.page.get_by_placeholder("Provide details for this").click()
    #     self.page.get_by_placeholder("Provide details for this").fill("automated test error - 0")
    #     self.page.get_by_placeholder("Provide possible solution").click()
    #     self.page.get_by_placeholder("Provide possible solution").fill("test solution")
    #     self.page.get_by_placeholder("Enter sort order (number, e.g").click()
    #     self.page.get_by_placeholder("Enter sort order (number, e.g").fill("0")
    #     self.page.get_by_label("Platform *").select_option("2")
    #     self.page.get_by_label("Status *").select_option("false")
    #     self.page.get_by_text("Error Code *Error Code").click()
    #     self.page.get_by_label("Status *").select_option("true")
    #     self.page.get_by_role("button", name="Submit").click()
    #     self.page.get_by_text("Inactive", exact=True).click()
    #     self.page.get_by_text("Active", exact=True).click()
    #     self.page.get_by_role("cell", name="1050").click()
    #     self.page.get_by_role("cell", name="automated test error -").click()
    #     self.page.get_by_role("row", name="1050 automated test error - 0").get_by_role("button").click()
    #     self.page.locator("div").filter(has_text="Status Changed").nth(3).click()
    #     self.page.get_by_text("Inactive", exact=True).click()
    #     self.page.get_by_role("cell", name="automated test error -").click()
    #     self.page.get_by_role("row", name="1050 automated test error - 0").get_by_role("button").click()
    #     self.page.get_by_text("Status Changed").click()
    #     self.page.get_by_text("Active", exact=True).click()
    #     self.page.get_by_role("cell", name="automated test error -").click()
    #     self.page.get_by_text("Inactive", exact=True).click()
    #     self.page.get_by_text("Active", exact=True).click()
    #     self.page.get_by_text("Error Guide List").click()

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
        self.page.pause()
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
        self.page.get_by_placeholder("Provide an image file").click()
        self.page.get_by_placeholder("Provide an image file").set_input_files(r"files\rdms_logo.png")

    def videoFAQAnswer(self):
        self.page.get_by_label("FAQ Type *").select_option('VIDEO')
        self.page.get_by_placeholder("Provide a youtube video link").click()
        self.page.get_by_placeholder("Provide a youtube video link").fill("https://youtu.be/rmC5bLymUgs?si=Q8wSP7NiPHd72o-H")

    def confirmNewFAQ(self):
        expect(self.page.get_by_text("Created Successfully")).to_be_visible()
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
        expect(self.page.get_by_text("Created Successfully")).to_be_visible()
        self.page.get_by_text("Created Successfully").click()
        row = self.page.locator(f"tr:has-text('{name}')")
        expect(row.locator("td:nth-child(2)")).to_contain_text(f"{name}_edit")

        # self.page.get_by_label("FAQ Type *").select_option("PICTURE")
        # self.page.get_by_label("FAQ Type *").select_option("VIDEO")
        # self.page.get_by_label("FAQ Type *").select_option("BASIC")
        # self.page.get_by_placeholder("Type your question..").click()
        # self.page.get_by_placeholder("Type your question..").fill("automated test question - 0")
        # self.page.get_by_placeholder("Provide answer to your").click()
        # self.page.get_by_placeholder("Provide answer to your").fill("test answer")
        # self.page.get_by_label("Platform *").select_option("RDMS")
        # self.page.get_by_placeholder("Enter sort order (number, e.g").click()
        # self.page.get_by_placeholder("Enter sort order (number, e.g").fill("0")
        # self.page.get_by_role("button", name="Submit").click()


        # self.page.get_by_role("cell", name="automated test question -").click()
        # self.page.get_by_role("row", name="59 automated test question -").get_by_role("button").click()
        # self.page.get_by_text("Inactive", exact=True).click()
        # self.page.get_by_role("cell", name="automated test question -").click()
        # self.page.get_by_role("cell", name=" Activate").nth(1).click()
        # self.page.get_by_text("Active", exact=True).click()
        # self.page.locator("#o5gvgqtuzh").click()
        # self.page.locator("tr:nth-child(6) > td:nth-child(4)").click(button="right")
        # self.page.get_by_text("ActiveInactiveFAQ").click()
        # self.page.get_by_role("row", name="59 automated test question -").get_by_role("button").click()
        # self.page.get_by_text("Status Changed").click()
        # self.page.get_by_role("link", name="Error Guide").click()
        # self.page.get_by_role("link", name="Add New").click()
        # self.page.get_by_role("link", name="FAQ").click()
        # self.page.get_by_text("Inactive", exact=True).click()
        # self.page.get_by_role("row", name="59 automated test question -").get_by_role("link").click()
        # self.page.get_by_placeholder("Type your question..").click()
        # self.page.get_by_placeholder("Type your question..").fill("automated test question - 0 - edited")
        # self.page.get_by_role("button", name="Update").click()
        # self.page.get_by_text("Inactive", exact=True).click()
        # self.page.get_by_role("row", name="59 automated test question -").get_by_role("link").click()
        # self.page.get_by_label("Status *").select_option("true")
        # self.page.get_by_role("button", name="Update").click()
        # self.page.get_by_text("Created Successfully").click()
        # self.page.get_by_role("cell", name="automated test question - 0").click()

    #     self.page.get_by_text("Field Force App").click()
    #     self.page.get_by_role("link", name="FAQ").click()
    #     self.page.get_by_role("row", name="61 automated test question -").get_by_role("link").click()
    #     self.page.get_by_placeholder("Type your question..").click()
    #     self.page.get_by_placeholder("Type your question..").fill("automated test question - 1 - edited")
    #     self.page.locator("#main-content div").filter(has_text="FAQ Type *--Select FAQ Type--").nth(2).click()
    #     self.page.locator("#main-content div").filter(has_text="FAQ Type *--Select FAQ Type--").nth(2).click()
    #     self.page.get_by_role("button", name="Update").click()
    #     self.page.locator("div").filter(has_text="Created Successfully").nth(3).click()
    #     self.page.get_by_role("row", name="60 automated test question").get_by_role("link").click()
    #     self.page.get_by_label("FAQ Type *").select_option("PICTURE")
    #     self.page.get_by_role("button", name="Choose File").click()
    #     self.page.locator("body").set_input_files("Screenshot 2024-11-18 093426.png")
    #     self.page.get_by_role("button", name="Update").click()
    #     self.page.get_by_text("Created Successfully").click()
    #     self.page.get_by_role("row", name="60 automated test question").get_by_role("link").click()
    #     self.page.get_by_text("null").click()
    #     self.page.locator("body").set_input_files("Screenshot 2024-11-18 093426.png")
    #     self.page.get_by_role("button", name="Update").click()
    #     self.page.get_by_text("Failed to create").click()
    #     self.page.get_by_role("button", name="Choose File").click()
    #     self.page.get_by_role("button", name="Update").click()
    #     self.page.get_by_text("Picture (only jpg/png) *Choose FileScreenshot 2024-11-18 093426.png").click()
    #     self.page.locator("body").set_input_files([])
    #     self.page.get_by_text("Picture (only jpg/png) *").click(button="right")
    #     self.page.get_by_role("button", name="Cancel").click()
    #     self.page.get_by_role("row", name="59 automated test question -").get_by_role("link").click()
    #     self.page.get_by_role("button", name="Cancel").click()
    #     self.page.get_by_role("row", name="60 automated test question").get_by_role("link").click()
    #     self.page.get_by_role("button", name="Choose File").click()
    #     self.page.locator("body").set_input_files("Screenshot 2024-11-18 093426.png")
    #     self.page.get_by_text("CancelUpdate").click()
    #     self.page.get_by_role("button", name="Update").click()
    #     self.page.get_by_role("button", name="Cancel").click()
    #     self.page.get_by_role("link", name="Add New").click()
    #     self.page.get_by_label("FAQ Type *").select_option("PICTURE")
    #     self.page.get_by_placeholder("Type your question..").click()
    #     self.page.get_by_placeholder("Type your question..").fill("test question - image")
    #     self.page.get_by_placeholder("Provide an image file").click()
    #     self.page.get_by_placeholder("Provide an image file").set_input_files("Screenshot 2024-11-18 093426.png")
    #     self.page.get_by_label("Platform *").select_option("RDMS")
    #     self.page.get_by_placeholder("Enter sort order (number, e.g").click()
    #     self.page.get_by_placeholder("Enter sort order (number, e.g").fill("0")
    #     self.page.get_by_role("button", name="Submit").click()
    #     self.page.get_by_role("row", name="62 test question - image").get_by_role("link").click()
    #     self.page.get_by_role("button", name="Choose File").click()
    #     self.page.locator("body").set_input_files("Capture2.PNG")
    #     self.page.get_by_role("button", name="Update").click()
    #     self.page.get_by_role("row", name="59 automated test question -").get_by_role("link").click()
    #     self.page.get_by_label("FAQ Type *").select_option("PICTURE")
    #     self.page.get_by_role("button", name="Choose File").click()
    #     self.page.locator("body").set_input_files("Screenshot 2024-11-18 093426.png")
    #     self.page.get_by_role("button", name="Update").click()
    #     self.page.get_by_role("row", name="60 automated test question").get_by_role("link").click()
    #     self.page.get_by_role("button", name="Choose File").click()
    #     self.page.get_by_role("button", name="Cancel").click()

    # self.page.get_by_role("link", name="FAQ").click()
    # self.page.get_by_role("row", name="60 automated test question").get_by_role("link").click()
    # self.page.get_by_label("FAQ Type *").select_option("VIDEO")
    # self.page.get_by_placeholder("Provide a youtube video link").click()
    # self.page.get_by_placeholder("Provide a youtube video link").fill("youtube.com")
    # self.page.get_by_role("button", name="Update").click()
    # self.page.get_by_placeholder("Provide a youtube video link").click()
    # self.page.get_by_placeholder("Provide a youtube video link").press("ArrowLeft")
    # self.page.get_by_placeholder("Provide a youtube video link").press("ArrowLeft")
    # self.page.get_by_placeholder("Provide a youtube video link").press("ArrowLeft")
    # self.page.get_by_placeholder("Provide a youtube video link").press("ArrowLeft")
    # self.page.get_by_placeholder("Provide a youtube video link").press("ArrowLeft")
    # self.page.get_by_placeholder("Provide a youtube video link").press("ArrowLeft")
    # self.page.get_by_placeholder("Provide a youtube video link").press("ArrowLeft")
    # self.page.get_by_placeholder("Provide a youtube video link").press("ArrowLeft")
    # self.page.get_by_text("Must be a valid URL").click()
    # self.page.get_by_placeholder("Provide a youtube video link").click()
    # self.page.get_by_placeholder("Provide a youtube video link").press("ArrowLeft")
    # self.page.get_by_placeholder("Provide a youtube video link").press("ArrowLeft")
    # self.page.get_by_placeholder("Provide a youtube video link").press("ArrowLeft")
    # self.page.get_by_placeholder("Provide a youtube video link").press("ArrowLeft")
    # self.page.get_by_placeholder("Provide a youtube video link").press("ArrowLeft")
    # self.page.get_by_placeholder("Provide a youtube video link").press("ArrowLeft")
    # self.page.get_by_placeholder("Provide a youtube video link").press("ArrowLeft")
    # self.page.get_by_placeholder("Provide a youtube video link").press("ArrowLeft")
    # self.page.get_by_placeholder("Provide a youtube video link").press("ArrowLeft")
    # self.page.get_by_placeholder("Provide a youtube video link").fill("https://youtube.com")
    # self.page.get_by_role("button", name="Update").click()
    # self.page.locator("#mmomd877lm").click()
    # self.page.get_by_role("button", name="Cancel").click()
    # self.page.get_by_role("row", name="59 automated test question -").get_by_role("link").click()
    # self.page.get_by_label("FAQ Type *").select_option("VIDEO")
    # self.page.get_by_placeholder("Provide a youtube video link").click()
    # self.page.get_by_placeholder("Provide a youtube video link").fill("https://youtube.com")
    # self.page.get_by_role("button", name="Update").click()
    # self.page.get_by_placeholder("Provide a youtube video link").click()
    # self.page.locator("div").filter(has_text=re.compile(r"^Question\*$")).click(button="right")
    # self.page.get_by_text("CancelUpdate").click()
    # self.page.get_by_role("button", name="Cancel").click()
    # self.page.get_by_role("row", name="61 automated test question -").get_by_role("link").click()
    # self.page.get_by_label("FAQ Type *").select_option("VIDEO")
    # self.page.get_by_placeholder("Provide a youtube video link").click()
    # self.page.get_by_placeholder("Provide a youtube video link").fill("https://www.youtube.com")
    # self.page.get_by_role("button", name="Update").click()