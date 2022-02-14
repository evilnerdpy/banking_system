import datetime
from database_app.database_functions import get_main_database
from database_app.database_functions import add_new_user_in_main_database
from database_app.database_functions import add_new_user_in_user_personal_details_database
from database_app.database_functions import add_new_user_in_current_wallets_database


def check_if_string_is_in_right_form(banned_signs, string):
    for sign in banned_signs:
        if string.find(sign) != -1 or string.strip() == "":
            return False
    return True


def get_user_birth_date():
    getting_user_birth_date = True
    date = datetime.datetime
    while getting_user_birth_date:
        day_of_birth = input("Please, enter  DAY of birth: ")
        month_of_birth = input("Please, enter birth MONTH NUMBER: ")
        year_of_birth = input("Please, enter  YEAR of birth: ")

        if not (day_of_birth.isdigit() and month_of_birth.isdigit() and year_of_birth.isdigit()):
            print("Prohibited symbols have been used, please try again")
            continue

        try:
            date = datetime.datetime(int(year_of_birth), int(month_of_birth), int(day_of_birth))
            getting_user_birth_date = False
        except ValueError:
            print("There is a mistake in your birthday date , please fill the form one more time")
            continue
    return date


def user_registration_confirmation(new_user_info):
    registration_form_confirmation_is_running = True
    while registration_form_confirmation_is_running:
        print('###################')
        print("This is new user information (username, password, privilege mode, account status):")
        print(new_user_info)
        confirmation_status = input("Please, confirm if this form is correct,\n"
                                    "otherwise you can fill this form one more time\n"
                                    "1.Confirm\n"
                                    "2.Decline\n")
        if confirmation_status == "1":
            print("This information will be added in main database")
            print("###################")
            return True
        elif confirmation_status == "2":
            print("Returning to registration menu")
            print("###################")
            return False


def check_if_identifier_is_unique(identifier):
    main_database = get_main_database()
    for line in main_database:
        current_user = line.split(",")
        if current_user[0] == identifier:
            return  False
    return True


def create_new_user(privilege):
    registration_menu_is_running = True
    banned_signs = [",", "_", " "]
    while registration_menu_is_running:
        print("###################")
        print(f"This menu is for creating {privilege} accounts!\n"
              "In order to create an account, please type in some personal information\n"
              f"Please, make sure you don't use {banned_signs} "
              f"characters and empty fields in your personal information.")

        username = input("Please, enter user name: ")
        if not check_if_string_is_in_right_form(banned_signs, username):
            print("Prohibited symbols have been used, please try again")
            continue

        second_name = input("Please, enter user second name: ")
        if not check_if_string_is_in_right_form(banned_signs, username):
            print("Prohibited symbols have been used, please try again")
            continue

        user_birth_date = get_user_birth_date()

        user_email = input("Please, enter user email: ")
        if not check_if_string_is_in_right_form(banned_signs, username):
            print("Prohibited symbols have been used, please try again")
            continue

        user_password = username + user_birth_date.strftime('%m/%d/%Y')
        user_unique_identifier = username + " " + second_name

        if not check_if_identifier_is_unique(user_unique_identifier):
            print("This user is already exist, please check new user personal information and try one more time")
            continue

        new_user_info_to_main_database = f"{user_unique_identifier},{user_password},{privilege},active"
        new_user_menu_to_user_personal_details_database = f"{user_unique_identifier}," \
                                                          f"{user_birth_date.strftime('%m/%d/%Y')},{user_email}"
        if user_registration_confirmation(new_user_info_to_main_database):
            add_new_user_in_main_database(new_user_info_to_main_database)
            add_new_user_in_user_personal_details_database(new_user_menu_to_user_personal_details_database)
            add_new_user_in_current_wallets_database(user_unique_identifier)
            registration_menu_is_running = False
        else:
            registration_menu_is_running = False
