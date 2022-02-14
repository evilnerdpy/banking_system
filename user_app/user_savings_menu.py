from database_app.database_functions import add_new_user_in_savings_wallets_database
from database_app.database_functions import deposit_and_withdrawal_money_on_savings_account
from database_app.database_functions import get_user_savings_wallet


def user_savings_menu(user):
    user_savings_menu_is_running = True
    while user_savings_menu_is_running:
        user_current_wallet = get_user_savings_wallet(user[0])
        if user_current_wallet == -1:
            add_new_user_in_savings_wallets_database(user[0])
            user_current_wallet = get_user_savings_wallet(user[0])
        print(f"Dear,{user[0]}!\n"
              f"This is the menu for operations with the savings wallet!\n"
              f"Your balance is {user_current_wallet[1]} RM!\n"
              f"Please , choose what you want to do...\n"
              f"1.Make a deposit\n"
              f"2.Make a withdrawal\n"
              f"3.Back to main page")
        selected_option = input("Enter your option: ")
        if selected_option == "1":
            user_deposit_menu(user)
        elif selected_option == "2":
            user_withdrawal_menu(user, float(user_current_wallet[1]))
        elif selected_option == "3":
            return
        else:
            print("Invalid input, please try again")


def check_if_deposit_value_is_in_right_form(deposit):
    try:
        if float(deposit) <= 0:
            return False
        return True
    except ValueError:
        return False


def check_if_withdrawal_value_is_in_right_form(withdrawal, user_balance):
    try:
        if (user_balance - float(withdrawal) > 100) and float(withdrawal) > 0:
            return True
        print("Not enough money on the balance.\n"
              "Minimum balance for current wallet is 100RM")
        return False
    except ValueError:
        return False


def user_deposit_menu(user):
    deposit_value = input("Please , type how many RM you want to deposit: ")
    if not check_if_deposit_value_is_in_right_form(deposit_value):
        print("Invalid input, please try again")
        return
    deposit_and_withdrawal_money_on_savings_account(user[0], deposit_value, "deposit")


def user_withdrawal_menu(user, balance):
    withdrawal_value = input("Please , type how many RM you want to withdrawal: ")
    if not check_if_withdrawal_value_is_in_right_form(withdrawal_value, balance):
        print("Invalid input, please try again")
        return
    deposit_and_withdrawal_money_on_savings_account(user[0], withdrawal_value, "withdrawal")