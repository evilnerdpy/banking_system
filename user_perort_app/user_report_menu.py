import datetime
from database_app.database_functions import get_user_savings_wallet
from database_app.database_functions import get_user_current_wallet


def user_report_menu(user_identifier, wallet_type):

    user_wallet = []
    if wallet_type == "savings":
        user_wallet = get_user_savings_wallet(user_identifier)
    elif wallet_type == "current":
        user_wallet = get_user_current_wallet(user_identifier)

    if user_wallet == -1:
        print("There is no information about " + user_identifier + " " + wallet_type + "wallet")
        return
    transactions = user_wallet[2:len(user_wallet)]
    if not transactions:
        print("No transactions were made on this wallet.Nothing to print yet!")
        return

    start_date = get_day("start")
    end_date = get_day("end")
    if end_date < start_date:
        print("End date should be later then start date!")
        return
    print_report(start_date, end_date, transactions)
    input("Pres ENTER to return to main menu")


def check_if_date_is_in_right_form(day, month, year):
    try:
        datetime.datetime(int(year), int(month), int(day))
        return True
    except ValueError:
        return False


def get_day(condition):
    while True:
        day = input(f"Please enter {condition} date DAY: ")
        month = input(f"Please enter {condition} date MONTH: ")
        year = input(f"Please enter {condition} date YEAR: ")
        if check_if_date_is_in_right_form(day, month, year):
            if condition == "start":
                date = datetime.datetime(int(year), int(month), int(day))
                return date
            elif condition == "end":
                date = datetime.datetime(int(year), int(month), int(day), 23, 59)
                return date
        print("Invalid date, please try one more time")


def print_report(start_date, end_date, transactions):
    counter = 1
    for transaction in transactions:
        current_transaction = transaction.split("_")
        current_transaction_date = datetime.datetime.strptime(current_transaction[0], "%y/%d/%m-%H:%M")
        if start_date <= current_transaction_date <= end_date:
            print(f"{counter}.Transaction time - {current_transaction_date},\n"
                  f"Transaction type - {current_transaction[1]}\n"
                  f"Transaction amount - {current_transaction[2]}")
            counter += 1
