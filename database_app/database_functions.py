import datetime


def create_default_superuser():
    # account number, password, privilege
    return "admin,admin,super_user,active"


def default_super_user_personal_details():
    return "Mark Stepanov,11/08/2002,markstepanov88@gmail.com"


def get_main_database():
    while True:
        try:
            with open("main_database.txt", "r") as main_database:
                users = main_database.readlines()
                list_to_return = []
                for user in users:
                    list_to_return.append(user.replace("\n", ""))
                return list_to_return
        except FileNotFoundError:
            with open("main_database.txt", "w") as main_database:
                main_database.write(create_default_superuser())
                main_database.write("\n")
        

def write_to_main_database(users):
    with open("main_database.txt", "w") as registration_db:
        registration_db.write('\n'.join(users))


def get_user_from_database(number, password):
    users = get_main_database()
    for user in users:
        current_user = user.split(",")
        if current_user[0] == number and current_user[1] == password and current_user[3] == "active":
            return current_user

    return -1


def get_user_personal_details_database():
    while True:
        try:
            with open("user_personal_details_database.txt", "r") as personal_database:
                users = personal_database.readlines()
                list_to_write = []
                for user in users:
                    list_to_write.append(user.replace("\n", ""))
                return list_to_write
        except FileNotFoundError:
            with open("user_personal_details_database.txt", "w") as personal_database:
                personal_database.write(default_super_user_personal_details())
                personal_database.write("\n")


def write_to_user_personal_details_database(user):
    with open("user_personal_details_database.txt", "w") as personal_database:
        personal_database.write('\n'.join(user))


def add_new_user_in_main_database(user_info):
    all_users = get_main_database()
    all_users.append(user_info)
    list_to_write = []
    for user in all_users:
        list_to_write.append(user.replace("\n", ""))
    write_to_main_database(list_to_write)


def add_new_user_in_user_personal_details_database(user_info):
    all_users = get_user_personal_details_database()
    all_users.append(user_info)
    list_to_write = []
    for user in all_users:
        list_to_write.append(user.replace("\n", ""))
    write_to_user_personal_details_database(list_to_write)


def change_line_in_main_database(line_to_write, line_to_delete):
    line_to_delete = line_to_delete.replace("\n", "")
    main_database = get_main_database()
    list_to_write = []
    for line in main_database:
        if line == line_to_delete:
            list_to_write.append(line_to_write.replace("\n", ""))
            continue
        list_to_write.append(line.replace("\n", ""))
    with open("main_database.txt", "w") as db:
        db.write("\n".join(list_to_write))


def change_line_in_personal_details_database(line_to_write, line_to_delete):
    line_to_delete = line_to_delete.replace("\n", "")
    main_database = get_user_personal_details_database()
    list_to_write = []
    for line in main_database:
        if line == line_to_delete:
            list_to_write.append(line_to_write.replace("\n", ""))
            continue
        list_to_write.append(line.replace("\n", ""))
    with open("user_personal_details_database.txt", "w") as db:
        db.write("\n".join(list_to_write))


def get_current_wallets_database():
    while True:
        try:
            with open("current_wallets_database.txt", "r") as current_wallets_database:
                wallets = current_wallets_database.readlines()
            list_to_send = []
            for wallet in wallets:
                list_to_send.append(wallet.replace("\n", ""))
            return list_to_send
        except FileNotFoundError:
            with open("current_wallets_database.txt", "w"):
                pass


def get_savings_wallets_database():
    while True:
        try:
            with open("savings_wallets_database.txt", "r") as savings_wallets_database:
                wallets = savings_wallets_database.readlines()
            list_to_send = []
            for wallet in wallets:
                list_to_send.append(wallet.replace("\n", ""))
            return list_to_send
        except FileNotFoundError:
            with open("savings_wallets_database.txt", "w"):
                pass


def get_user_current_wallet(user_identifier):
    current_wallets_database = get_current_wallets_database()
    for wallet in current_wallets_database:
        current_wallet = wallet.split(",")
        if current_wallet[0] == user_identifier:
            return current_wallet
    return -1


def get_user_savings_wallet(user_identifier):
    savings_wallets_database = get_savings_wallets_database()
    for wallet in savings_wallets_database:
        current_savings_wallet = wallet.split(",")
        if current_savings_wallet[0] == user_identifier:
            return current_savings_wallet
    return -1


def write_to_current_wallets_database(list_to_write):
    with open("current_wallets_database.txt", "w") as current_wallets_db:
        current_wallets_db.write('\n'.join(list_to_write))


def write_to_savings_database(list_to_write):
    with open("savings_wallets_database.txt", "w") as savings_wallets_db:
        savings_wallets_db.write("\n".join(list_to_write))


def add_new_user_in_current_wallets_database(user_info):
    all_wallets = get_current_wallets_database()
    all_wallets.append(f"{user_info},0")
    list_to_write = []
    for user in all_wallets:
        list_to_write.append(user.replace("\n", ""))
    write_to_current_wallets_database(list_to_write)


def add_new_user_in_savings_wallets_database(user_info):
    all_wallets = get_savings_wallets_database()
    all_wallets.append(f"{user_info},0")
    list_to_write = []
    for user in all_wallets:
        list_to_write.append(user.replace("\n", ""))
    write_to_savings_database(list_to_write)


def deposit_and_withdrawal_money_on_current_account(user_identifier, amount, action):
    current_wallets_database = get_current_wallets_database()
    list_of_wallets_to_write = []
    current_amount = float(amount)
    if action == "withdrawal":
        current_amount *= -1
    for wallet in current_wallets_database:
        current_wallet = wallet.split(",")
        if current_wallet[0] == user_identifier:
            previous_transactions = ",".join(current_wallet[2:len(current_wallet)])
            if previous_transactions != "":
                previous_transactions += ","
            else:
                previous_transactions = ""
            new_wallet_value = f"{user_identifier},{str(round(float(current_wallet[1]) + float(current_amount), 4))}," \
                               f"{previous_transactions}" \
                               f"{datetime.datetime.now().strftime('%y/%d/%m-%H:%M')}_{action.upper()}_{amount}"
            list_of_wallets_to_write.append(new_wallet_value)
            continue
        list_of_wallets_to_write.append(wallet)

    with open("current_wallets_database.txt", "w") as current_db:
        current_db.write("\n".join(list_of_wallets_to_write))


def deposit_and_withdrawal_money_on_savings_account(user_identifier, amount, action):
    current_wallets_database = get_savings_wallets_database()
    list_of_wallets_to_write = []
    current_amount = float(amount)
    if action == "withdrawal":
        current_amount *= -1
    for wallet in current_wallets_database:
        current_wallet = wallet.split(",")
        if current_wallet[0] == user_identifier:
            previous_transactions = ",".join(current_wallet[2:len(current_wallet)])
            if previous_transactions != "":
                previous_transactions += ","
            else:
                previous_transactions = ""
            new_wallet_value = f"{user_identifier},{str(round(float(current_wallet[1]) + float(current_amount), 4))}," \
                               f"{previous_transactions}" \
                               f"{datetime.datetime.now().strftime('%y/%d/%m-%H:%M')}_{action.upper()}_{amount}"
            list_of_wallets_to_write.append(new_wallet_value)
            continue
        list_of_wallets_to_write.append(wallet)

    with open("savings_wallets_database.txt", "w") as current_db:
        current_db.write("\n".join(list_of_wallets_to_write))
