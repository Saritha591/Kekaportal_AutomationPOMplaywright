from data import config


class KekaportalhomePage:

    username = config.username
    password = config.password

    def __init__(self, page):
        self.page = page
        self.homepage = page.locator(
            "//span[@class='ki-home sidebar-list-icon']")
        self.homepage_gotoBirthdays = page.locator(
            "//p[@class='text-large text-dark']")
        
    def home_Pagelocator(self):
        self.homepage.click()
        self.homepage_gotoBirthdays.click()