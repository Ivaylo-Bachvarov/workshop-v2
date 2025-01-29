from .constants import BASE_URL


class GuestListPage:
    def __init__(self, page):
        self.page = page
        self.url = BASE_URL + "/admin/reservations/guest/"

    def add_guest_button(self):
        return self.page.locator('#content-main > ul > li > a')

    def success_message(self):
        return self.page.locator("#content-start > ul > li")
