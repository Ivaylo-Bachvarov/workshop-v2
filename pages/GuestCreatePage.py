from .constants import BASE_URL


class GuestCreatePage:
    def __init__(self, page):
        self.page = page
        self.url = BASE_URL + "/admin/reservations/guest/add/"

    def first_name_field(self):
        return self.page.locator("#id_first_name")

    def last_name_field(self):
        return self.page.locator("#id_last_name")

    def email_field(self):
        return self.page.locator("#id_email")

    def phone_field(self):
        return self.page.locator("#id_phone")

    def save_button(self):
        return self.page.locator("#guest_form > div > div > input.default")
