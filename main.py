from login_app.login_menu import login_menu


def greetings_page():
    print("###################\n"
          "Welcome to MARK STEPANOV BANK!\n"
          "We are very happy that you choose us!\n"
          "Please login to move further...")


def run_banking_system():
    banking_system_is_running = True
    greetings_page()
    while banking_system_is_running:
        selected_option = input("###################\n"
                                "1.Log in\n"
                                "2.I don't have an account\n"
                                "Please choose an option: ")

        if selected_option == "1":
            login_menu()
        elif selected_option == "2":
            print("###################\n"
                  "Please contact a bank employee and provide him with the information necessary for registration,\n"
                  "now you will be returned to registration page\n"
                  "press ENTER key to continue")
        else:
            print("Invalid input, please try again")


if __name__ == "__main__":
    run_banking_system()
