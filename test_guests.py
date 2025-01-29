from playwright.sync_api import Page, expect

from pages.GuestCreatePage import GuestCreatePage
from pages.GuestListPage import GuestListPage
from pages.LoginPage import LoginPage
from pages.HomePage import HomePage
from pages.constants import ROOT_USERNAME, ROOT_PASSWORD
from sdk import nuke_database


def test_create_guest(page: Page):
    login_page = LoginPage(page)
    login_page.goto()

    login_page.login_field().fill(ROOT_USERNAME)
    login_page.password_field().fill(ROOT_PASSWORD)
    login_page.submit_button().click()

    home_page = HomePage(page)
    expect(page).to_have_url(home_page.url)

    nuke_database(page)

    home_page.guest_list_button().click()

    guest_list_page = GuestListPage(page)
    guest_list_page.add_guest_button().click()

    guest_create_page = GuestCreatePage(page)
    expect(page).to_have_url(guest_create_page.url)

    guest_create_page.first_name_field().fill("Ivaylo")
    guest_create_page.last_name_field().fill("Bachvarov")
    guest_create_page.email_field().fill("ivaylo@example.com")
    guest_create_page.phone_field().fill("0888888888")
    guest_create_page.save_button().click()

    expect(page).to_have_url(guest_list_page.url)
    expect(guest_list_page.success_message()).to_be_visible()