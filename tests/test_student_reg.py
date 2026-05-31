from pages.registration_page import RegistrationPage
from test_data.student_data import student_data


def test_student_registration(page):

    form = RegistrationPage(page)

    form.navigate()

    form.enter_name(
        student_data["first_name"],
        student_data["last_name"]
    )

    form.enter_email(
        student_data["email"]
    )

    form.select_gender(
        student_data["gender"]
    )

    form.enter_mobile(
        student_data["mobile"]
    )

    form.select_dob(
        student_data["dob_day"],
        student_data["dob_month"],
        student_data["dob_year"]
    )

    form.enter_subject(
        student_data["subject"]
    )

    form.select_hobbies(
        student_data["hobbies"]
    )

    form.upload_picture(
        "scrre.png"
    )

    form.enter_address(
        student_data["address"]
    )

    form.select_state(
        student_data["state"]
    )

    form.select_city(
        student_data["city"]
    )

    form.submit_form()

    form.validate_success_popup()