from libs.goto_loginpage_kekaportal import KekaportalloginPage
from libs.homepage_kekaportal import KekaportalhomePage
from libs.mepage_kekaportal import KekaportalMePage
from libs.inboxpage_kekaportal import KekaportalinboxPage
from data import config

username = config.username
password = config.password


def test_inboxtab(page):
    portal = KekaportalloginPage(page)
    portal_1 = KekaportalhomePage(page)
    portal_2 = KekaportalMePage(page)
    portal_3 = KekaportalinboxPage(page)
    portal.kekaportalbtn()
    portal.login_details(username, password)
    portal_1.home_Pagelocator()
    portal_2.attendence()
    portal_3.TakeAction_inbox()
