import time
from playwright.sync_api import sync_playwright

def test_open_example():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        page.goto("https://www.google.com/")
        time.sleep(2)
        # assert "Example Domain" in page.title()
        browser.close()
