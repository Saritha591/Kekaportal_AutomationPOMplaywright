from data import config


class KekaportalhomePage:

    username = config.username
    password = config.password

    def __init__(self, page):
        self.page = page
        self.homepage = page.locator(
            "//span[@class='ic-home sidebar-list-icon']")
        self.homepage_gotoBirthdays = page.locator(
            "//span[@class='icon ic-cake icon-xxs icon-accent-red']")
        
    def home_Pagelocator(self):
        self.homepage.click()
        self.homepage_gotoBirthdays.click()