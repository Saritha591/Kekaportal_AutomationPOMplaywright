from libs.goto_loginpage_kekaportal import KekaportalloginPage
from libs.homepage_kekaportal import KekaportalhomePage
from libs.mepage_kekaportal import KekaportalMePage
from libs.inboxpage_kekaportal import KekaportalinboxPage
from libs.myteams_kekaportal import KekaportalmyteamPage
from libs.orgpage_kekaportal import KekaportalorgPage
from playwright.sync_api import Page
from data import config

username = config.username
password = config.password

def test_orgpage(page):
    portal = KekaportalloginPage(page)
    portal_1 = KekaportalhomePage(page)
    portal_2 = KekaportalMePage(page)
    portal_3 = KekaportalinboxPage(page)
    portal_4 = KekaportalmyteamPage(page)
    portal_5 = KekaportalorgPage(page)
    portal.goto()
    portal.kekaportalbtn()
    portal_1.login_details(username,password)
    portal.home_Pagelocator()
    portal_2.attendence()
    portal_3.TakeAction_inbox()
    portal_4.Myteam_page()
    portal_5.Org_Employees()



