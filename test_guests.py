import requests
from time import sleep

from pages.GuestListPage import GuestListPage
from pages.LoginPage import LoginPage
from pages.HomePage import HomePage
from pages.constants import BASE_URL
from playwright.sync_api import Page, expect


def get_session(cookies):
    for cookie in cookies:
        if cookie["name"] == "sessionid":
            return cookie["value"]


def test_create_guest(page: Page):
    login_page = LoginPage(page)
    login_page.goto()

    login_page.login_field().fill("ivaylo")
    login_page.password_field().fill("qaworkshop")
    login_page.submit_button().click()

    home_page = HomePage(page)
    expect(page).to_have_url(home_page.url)
    session = get_session(page.context.cookies())

    headers = {"Cookie": "sessionid=" + session}
    requests.post(BASE_URL + "/api/nuke/", headers=headers)

    home_page.guest_list_button().click()

    guest_list_page = GuestListPage(page)
    guest_list_page.add_guest_button().click()

    first_name_field = page.locator("#id_first_name")
    first_name_field.fill("Ivaylo")

    last_name_field = page.locator("#id_last_name")
    last_name_field.fill("Bachvarov")

    email_field = page.locator("#id_email")
    email_field.fill("ivaylo@hacksoft.io")

    phone_field = page.locator("#id_phone")
    phone_field.fill("0888888888")

    save_button = page.locator("#guest_form > div > div > input.default")
    save_button.click()

    success_message = page.locator("#content-start > ul > li")
    expect(success_message).to_be_visible()
