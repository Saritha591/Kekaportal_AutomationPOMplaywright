from data import config


class KekaportalorgPage:

    username = config.username
    password = config.password

    def __init__(self, page):
        self.page = page
        self.org = page.locator(
            "//li[@class='nav-item active']//a[@class='nav-link']")
        self.org_emp = page.locator("//span[normalize-space()='Employees']")

    def Org_Employees(self):
        self.org.click()
        self.org_emp.press("Enter")
