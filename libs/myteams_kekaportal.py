from data import config


class KekaportalmyteamPage:

    username = config.username
    password = config.password

    def __init__(self, page):
        self.page = page
        self.teamtab = page.locator("//ul[@class='nav topnav']")
        
        

    def Myteam_page(self):
        self.teamtab.click()