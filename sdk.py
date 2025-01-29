import requests
from playwright.sync_api import Page

from pages.constants import BASE_URL


def get_session(cookies):
    for cookie in cookies:
        if cookie["name"] == "sessionid":
            return cookie["value"]


def nuke_database(page: Page):
    session = get_session(page.context.cookies())

    headers = {"Cookie": "sessionid=" + session}
    requests.post(BASE_URL + "/api/nuke/", headers=headers)
