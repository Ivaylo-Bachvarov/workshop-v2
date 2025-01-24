class GuestListPage:
    def __init__(self, page):
        self.page = page
    
    def add_guest_button(self):
        return self.page.locator('#content-main > ul > li > a')
