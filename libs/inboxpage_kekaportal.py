from data import config


class KekaportalinboxPage:

    username = config.username
    password = config.password

    def __init__(self, page):
        self.page = page
        self.inboxtab = page.locator("//span[@class='ki-inbox sidebar-list-icon']")
        self.Takeaction = page.locator("//a[@routerlink='action']")
        
    
    def TakeAction_inbox(self):
        self.inboxtab.click()
        self.Takeaction.click()
        
