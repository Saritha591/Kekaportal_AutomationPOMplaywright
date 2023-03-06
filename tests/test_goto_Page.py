from libs.goto_loginpage_kekaportal import KekaportalloginPage
from data import config

username = config.username
password = config.password


def test_goto_url(page):
    portal = KekaportalloginPage(page)
    portal.goto()
    portal.kekaportalbtn()
