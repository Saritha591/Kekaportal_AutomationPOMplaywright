from libs.goto_loginpage_kekaportal import KekaportalloginPage
from data import config

username = config.username
password = config.password


def test_login(page):
    portal = KekaportalloginPage(page)
    portal.kekaportalbtn()
    portal.login_details(username, password)
