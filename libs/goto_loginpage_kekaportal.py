from data import config


class KekaportalLoginPage:

    username = config.username
    password = config.password

    def __init__(self, page):
        self.page = page
        self.page.goto("https://msys.keka.com/")
        self.kekaportal = page.locator(
            "//p[normalize-space()='Keka Password']")
        self.username = page.locator("//input[@id='email']")
        self.password = page.locator("//input[@id='password']")
        self.loginbtn = page.locator("//button[normalize-space()='Login']")

    def kekaportalbtn(self):
        self.kekaportal.click()

    def login_details(self, username, password):
        self.username.fill(username)
        self.password.fill(password)
        self.loginbtn.click()


