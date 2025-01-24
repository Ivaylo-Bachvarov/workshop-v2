from .constants import BASE_URL


class HomePage:
    def __init__(self, page):
        self.page = page
        self.url = BASE_URL + '/admin/'
    
    def goto(self):
        self.page.goto(self.url)

    def guest_list_button(self):
        return self.page.locator('#reservations-guest > a')