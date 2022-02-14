from database_app.database_functions import get_main_database
from database_app.database_functions import get_user_personal_details_database
from database_app.database_functions import change_line_in_main_database, change_line_in_personal_details_database
from create_user_app.create_user_menu import check_if_string_is_in_right_form, get_user_birth_date


def prepare_user_info(user_identifier):
    current_user_personal_string = ""
    main_database = get_main_database()
    personal_details_database = get_user_personal_details_database()
    current_user_string = ""
    for user in main_database:
        current_user = user.split(",")
        if user_identifier == current_user[0]:
            current_user_string = user
    if current_user_string == "":
        return -1
    for user in personal_details_database:
        current_user = user.split(",")
        if current_user[0] == user_identifier:
            current_user_personal_string = user

    return current_user_personal_string, current_user_string


def change_user_information_menu(user_identifier, privilege):
    banned_signs = [",", "_", " "]
    change_user_information_menu_is_running = True
    if prepare_user_info(user_identifier) != -1:
        current_user_personal_string, current_user_main_string = prepare_user_info(user_identifier)
    else:
        print("Invalid information")
        return False
    current_user_main_database = current_user_main_string.split(",")
    current_user_personal_details_database = current_user_personal_string.split(",")
    while change_user_information_menu_is_running:
        print("###################")
        print(f"You want change information in '{current_user_main_database[0]}' account.\n"
              f"Current information is:\n"
              f"Name - {current_user_main_database[0]}, \n"
              f"Password - {current_user_main_database[1]}, \n"
              f"Date of Birth - {current_user_personal_details_database[1]}, \n"
              f"Email - {current_user_personal_details_database[2]}\n"
              f"Please, make sure you don't use {banned_signs}\n"
              f"characters and empty fields in your personal information.\n"
              f"Please, choose what you want to change:\n"
              f"1.Password\n"
              f"2.Date of Birth\n"
              f"3.Email\n"
              f"4.Apply changes\n"
              f"5.Return to previous menu")
        if privilege == "super_user":
            print("6.Account status")
        selected_option = input("Please choose an option: ")
        if selected_option == "1":
            current_user_main_database[1] = change_password(banned_signs)
        elif selected_option == "2":
            current_user_personal_details_database[1] = get_user_birth_date().strftime("%m/%d/%Y")
        elif selected_option == "3":
            current_user_personal_details_database[2] = change_email(banned_signs)
        elif selected_option == "4":
            data_to_change_to_main_database = ",".join(current_user_main_database)
            data_to_change_to_personal_details_database = ",".join(current_user_personal_details_database)
            change_line_in_main_database(data_to_change_to_main_database, current_user_main_string.strip())
            change_line_in_personal_details_database(data_to_change_to_personal_details_database,
                                                     current_user_personal_string)
        elif selected_option == "5":
            change_user_information_menu_is_running = False
            return False
        elif selected_option == "6" and privilege == "super_user":
            current_user_main_database[3] = change_account_status(current_user_main_database[3])

        else:
            print("Invalid input, please try again")
 


def change_password(banned_signs):
    while True:
        new_password = input("Please enter a password: ")
        if not check_if_string_is_in_right_form(banned_signs, new_password):
            print("Prohibited symbols have been used, please try again")
            continue
        return new_password


def change_email(banned_signs):
    while True:
        new_email = input("Please enter an email: ")
        if not check_if_string_is_in_right_form(banned_signs, new_email):
            print("Prohibited symbols have been used, please try again")
            continue
        return new_email


def change_account_status(status):
    while True:
        if status == "active":
            selected_option = input("Current account status is active, change to inactive?\n"
                                    "1.Confirm\n"
                                    "2.Decline\n"
                                    "Select an option: ")
            if selected_option == "1":
                return "inactive"
            elif selected_option == "2":
                return "active"
            else:
                print("Invalid input, please try again")
        elif status == "inactive":
            selected_option = input("Current account status is inactive, change to active?\n"
                                    "1.Confirm\n"
                                    "2.Decline\n"
                                    "Select an option: ")
            if selected_option == "1":
                return "active"
            elif selected_option == "2":
                return "inactive"
            else:
                print("Invalid input, please try again")

