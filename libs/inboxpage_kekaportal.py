from data import config


class KekaportalinboxPage:

    username = config.username
    password = config.password

    def __init__(self, page):
        self.page = page
        self.inboxtab = page.locator("//span[@class='ki-user sidebar-list-icon']")
        self.Takeaction = page.locator("//a[@routerlink='action']")
        self.notification = page.locator("//a[@routerlink='notifications']")
    
    def TakeAction_inbox(self):
        self.inboxtab.click()
        self.Takeaction.click()
        self.notification.click()
