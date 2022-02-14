from create_user_app.create_user_menu import create_new_user
from database_app.database_functions import get_main_database
from database_app.database_functions import get_user_personal_details_database
from create_user_app.change_user_information import change_user_information_menu


def super_user_menu(user):
    admin_menu_is_running = True
    while admin_menu_is_running:
        selected_option = input(f"Greetings, {user[0]}!\n"
                                f"You entered in super user mode\n"
                                f"Please, choose what you want to do...\n"
                                f"1.Create new staff user\n"
                                f"2.Show all users\n"
                                f"3.Change user information\n"
                                f"4.Back to registration menu\n"
                                f"Please,choose an option: ")
        if selected_option == "1":
            create_new_user("staff")
        elif selected_option == "2":
            show_all_users()
        elif selected_option == "3":
            find_user_to_change_information()
        elif selected_option == "4":
            return
        else:
            print("Invalid input, please try again")


def show_all_users():
    main_database = get_main_database()
    personal_information_database = get_user_personal_details_database()
    user_counter = 1
    for user in main_database:
        current_user = user.split(",")
        current_user[3] = current_user[3].replace('\n', '')
        print(f"{user_counter}.Account number - {current_user[0]},privilege mode - {current_user[2]}, "
              f"account status - {current_user[3]} ")
        user_counter += 1
        for personal_info in personal_information_database:
            current_personal_info = personal_info.split(",")
            current_personal_info[2] = current_personal_info[2].replace("\n", "")
            if current_personal_info[0] == current_user[0]:
                print(f"Name - {current_personal_info[0]}, date of birth - {current_personal_info[1]}, "
                      f"email - {current_personal_info[2]}")
    input("Pres ENTER to return to super user menu")


def find_user_to_change_information():
    identifier = input("Please enter user account number: ")
    change_user_information_menu(identifier, "super_user")


