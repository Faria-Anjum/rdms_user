from models.accessgroup import AccessGroupNMG, AccessGroupAM, SimActivationReportPage, AccessGroupPage

def test_NmgEditUserAccessGroup(page):
    nmg = AccessGroupNMG(page)
    nmg.navigate()
    nmg.loginUser()
    nmg.loginPass()
    nmg.clickSignIn()
    nmg.confirmSignedIn()
    agp = AccessGroupPage(page)
    agp.navigateToUserAccessGroup()

def test_removeAmSimActivationReportPermission(page):
    nmg = AccessGroupPage(page)
    nmg.editAMReportPermission()
    nmg.removeAmSimActivationReportPermission()

def test_checkAmSimActivationReportDisabled(page):
    am = AccessGroupAM(page)
    am.logout()
    am.loginUser()
    am.loginPass()
    am.clickSignIn()
    am.confirmSignedIn()
    sar = SimActivationReportPage(page)
    sar.simActivationReportNotVisible()

def test_giveAmSimActivationReportPermission(page):
    nmg = AccessGroupNMG(page)
    nmg.logout()
    nmg.navigate()
    nmg.loginUser()
    nmg.loginPass()
    nmg.clickSignIn()
    nmg.confirmSignedIn()
    agp = AccessGroupPage(page)
    agp.navigateToUserAccessGroup()
    agp.editAMReportPermission()
    agp.giveAmSimActivationReportPermission()

def test_checkAmSimActivationReportEnabled(page):
    am = AccessGroupAM(page)
    am.logout()
    am.loginUser()
    am.loginPass()
    am.clickSignIn()
    am.confirmSignedIn()
    sar = SimActivationReportPage(page)
    sar.simActivationReportVisible()
    am.logout()
