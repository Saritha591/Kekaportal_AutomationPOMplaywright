from data import config


class KekaportalMePage:

    username = config.username
    password = config.password

    def __init__(self, page):
        self.page = page
        self.MetabPage = page.locator(
            "//span[@class='ic-person sidebar-list-icon']")
        self.attendence_tab = page.locator(
            "//span[normalize-space()='Attendance']")

    def attendence(self):
        self.MetabPage.click()
        self.attendence_tab.click()
