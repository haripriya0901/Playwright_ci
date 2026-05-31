from playwright.sync_api import expect


class RegistrationPage:

    def __init__(self, page):

        self.page = page

    def navigate(self):

        self.page.goto(
            "https://demoqa.com/automation-practice-form"
        )

    def enter_name(self, first, last):

        self.page.locator("#firstName").fill(first)
        self.page.locator("#lastName").fill(last)

    def enter_email(self, email):

        self.page.locator("#userEmail").fill(email)

    def select_gender(self, gender):

        self.page.locator(
            f"input[value='{gender}']"
        ).check(force=True)

    def enter_mobile(self, mobile):

        self.page.locator("#userNumber").fill(mobile)

    def select_dob(self, day, month, year):

        self.page.locator("#dateOfBirthInput").click()

        self.page.locator(
            ".react-datepicker__year-select"
        ).select_option(year)

        self.page.locator(
            ".react-datepicker__month-select"
        ).select_option(month)

        self.page.locator(
            f".react-datepicker__day--0{day}"
        ).first.click()

    def enter_subject(self, subject):

        self.page.locator("#subjectsInput").fill(subject)

        self.page.keyboard.press("Enter")

    def select_hobbies(self, hobbies):

        hobby_map = {
            "Sports": "hobbies-checkbox-1",
            "Reading": "hobbies-checkbox-2",
            "Music": "hobbies-checkbox-3"
        }

        for hobby in hobbies:

            self.page.locator(
                f"label[for='{hobby_map[hobby]}']"
            ).click(force=True)

    def upload_picture(self, path):

        self.page.set_input_files(
            "#uploadPicture",
            path
        )

    def enter_address(self, address):

        self.page.locator(
            "#currentAddress"
        ).fill(address)

    def select_state(self, state):

        self.page.locator("#state").click()

        self.page.locator(
            f"text={state}"
        ).click()

    def select_city(self, city):

        self.page.locator("#city").click()

        self.page.locator(
            f"text={city}"
        ).click()

    def submit_form(self):

        self.page.locator("#submit").click()

    def validate_success_popup(self):

        expect(
            self.page.locator("#example-modal-sizes-title-lg")
        ).to_have_text(
            "Thanks for submitting the form"
        )