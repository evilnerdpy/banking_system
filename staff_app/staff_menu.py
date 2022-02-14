from create_user_app.create_user_menu import create_new_user
from create_user_app.change_user_information import change_user_information_menu
from super_user_app.super_user_menu import show_all_users
from user_perort_app.user_report_menu import user_report_menu


def staff_menu(user):
    staff_menu_is_running = True
    while staff_menu_is_running:
        selected_option = input(f"Greetings, {user[0]}!\n"
                                f"You entered in staff mode\n"
                                f"Please, choose what you want to do...\n"
                                f"1.Create new  user\n"
                                f"2.Change user information\n"
                                f"3.Show all users\n"
                                f"4.Print user report\n"
                                f"5.Back to registration menu\n"
                                f"Please,choose an option: ")
        if selected_option == "1":
            create_new_user("user")
        elif selected_option == "2":
            find_user_to_change_information()
        elif selected_option == "3":
            show_all_users()
        elif selected_option == "4":
            print_user_report()
        elif selected_option == "5":
            return
        else:
            print("Invalid input, please try again")


def find_user_to_change_information():
    identifier = input("Please enter user account number: ")
    value = change_user_information_menu(identifier, "staff")


def print_user_report():
    identifier = input("Please enter user account number: ")
    selected_option = input("Please, type report of which wallet do you want to know...\n"
                            "1.Current wallet\n"
                            "2.Savings wallet\n"
                            "Please,choose an option:")

    if selected_option == "1":
        user_report_menu(identifier, "current")
    elif selected_option == "2":
        user_report_menu(identifier, "savings")
    else:
        print("Invalid input, please try again")
