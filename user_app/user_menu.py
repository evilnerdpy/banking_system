from create_user_app.change_user_information import change_user_information_menu
from user_app.user_current_menu import user_current_menu
from user_app.user_savings_menu import user_savings_menu
from user_perort_app.user_report_menu import user_report_menu


def user_menu(user):
    user_menu_is_running = True
    while user_menu_is_running:
        selected_option = input(f"Greetings, {user[0]}!\n"
                                f"We are welcome you in our banking system!\n"
                                f"Please, choose what you want to do...\n"
                                f"1.Change my account information\n"
                                f"2.Operations with current account\n"
                                f"3.Operations with savings account\n"
                                f"4.Print a report\n"
                                f"5.Back to registration menu\n"
                                f"Please,choose an option: ")
        if selected_option == "1":
            change_user_information_menu(user[0], "user")
        elif selected_option == "2":
            user_current_menu(user)
        elif selected_option == "3":
            user_savings_menu(user)
        elif selected_option == "4":
            print_user_report(user[0])
        elif selected_option == "5":
            return
        else:
            print("Invalid input, please try again")


def print_user_report(user_identifier):
    selected_option = input("Please, type report of which wallet do you want to know...\n"
                            "1.Current wallet\n"
                            "2.Savings wallet\n"
                            "Please,choose an option:")
    if selected_option == "1":
        user_report_menu(user_identifier, "current")
    elif selected_option == "2":
        user_report_menu(user_identifier, "savings")
    else:
        print("Invalid input, please try again")
