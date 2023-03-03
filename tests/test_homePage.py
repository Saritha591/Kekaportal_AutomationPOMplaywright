from libs.goto_loginpage_kekaportal import KekaportalLoginPage
from libs.homepage_kekaportal import KekaportalhomePage

from data import config

username = config.username
password = config.password

def test_homepage(page):
    portal = KekaportalLoginPage(page)
    portal_1 = KekaportalhomePage(page)
    portal.kekaportalbtn()
    portal.login_details(username,password)
    portal_1.home_Pagelocator()
    