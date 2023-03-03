from libs.goto_loginpage_kekaportal import Kekaportal_LoginPage
from libs.homepage_kekaportal import Kekaportal_homePage
from libs.mepage_kekaportal import Kekaportal_MePage
from playwright.sync_api import Page
from data import config

username = config.username
password = config.password

def test_attendence(page):
    portal = KekaportalLoginPage(page)
    portal_1 = Kekaportal_homePage(page)
    portal_2 = Kekaportal_MePage(page)
    portal.goto()
    portal.kekaportalbtn()
    portal_1.login_details(username,password)
    portal.home_Pagelocator()
    portal_2.attendence()
