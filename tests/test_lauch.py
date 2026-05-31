import csv
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

def test_open_frame():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        page.goto("https://demo.automationtesting.in/Frames.html")
        time.sleep(2)
        frames = page.frame(name='SingleFrame')
        frames.locator("input[type='text']").fill("haripriya")
        # assert "Example Domain" in page.title()
        time.sleep(3)
        browser.close()

# def test_open_files():
#     with sync_playwright() as p:
#         browser = p.chromium.launch(headless=False)
#         page = browser.new_page()
#         page.goto("https://testautomationpractice.blogspot.com/")
#         time.sleep(2)
#         page.locator("input#singleFileInput").scroll_into_view_if_needed()

#         page.set_input_files('input#singleFileInput','files\search.txt')
#         print("file uploaded")
#         time.sleep(3)
#         browser.close()

def handle_alert(dialog):
    print("Alert says:", dialog.message)
    dialog.accept()

def test_handle_alerts():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        page.goto("https://testautomationpractice.blogspot.com/")
        time.sleep(2)
        # page.locator("input#singleFileInput").scroll_into_view_if_needed()

        # page.click('button#alertBtn')
        # page.once("dialog", handle_alert)
        page.once("button#alertBtn", lambda dialog: dialog.accept())
        page.screenshot(path="scrre.png")

        print("file uploaded")
        time.sleep(3)
        browser.close()

def read_csv_file(filepath):
    data=[]
    with open(filepath,newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            data.append(row)
        return data