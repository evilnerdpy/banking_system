from database_app.database_functions import get_user_from_database
from super_user_app.super_user_menu import super_user_menu
from staff_app.staff_menu import staff_menu
from user_app.user_menu import user_menu


def login_menu():
    acc_number = input("Please , enter your account number: ")
    password = input("Please enter your password: ")
    print("###################")
    user = get_user_from_database(acc_number, password)

    if user == -1:
        print("It appears your datta has been damaged, please contact staff")
        return
    user_privilege = user[2].replace("\n", "")
    if user_privilege == "super_user":
        super_user_menu(user)
    elif user_privilege == "staff":
        staff_menu(user)
    elif user_privilege == "user":
        user_menu(user)
