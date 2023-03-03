from libs.goto_loginpage_kekaportal import KekaportalLoginPage
from playwright.sync_api import Playwright, sync_playwright
from data import config

username = config.username
password = config.password


def test_goto_url(page):
    portal = KekaportalLoginPage(page)
    portal.goto()
    portal.kekaportalbtn()

    

