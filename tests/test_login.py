from libs.goto_loginpage_kekaportal import Kekaportal_LoginPage
from playwright.sync_api import Playwright, sync_playwright
from data import config

username = config.username
password = config.password


def test_login(page):
    portal = Kekaportal_LoginPage(page)
    portal.kekaportalbtn()
    portal.login_details(username,password)
    

