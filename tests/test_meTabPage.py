from libs.goto_loginpage_kekaportal import KekaportalloginPage
from libs.homepage_kekaportal import KekaportalhomePage
from libs.mepage_kekaportal import KekaportalMePage
from data import config

username = config.username
password = config.password


def test_attendence(page):
    portal = KekaportalloginPage(page)
    portal_1 = KekaportalhomePage(page)
    portal_2 = KekaportalMePage(page)
    portal.kekaportalbtn()
    portal.login_details(username, password)
    portal_1.home_Pagelocator()
    portal_2.attendence()
