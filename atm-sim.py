# ATM Challenge Requirements:
# User login with pin
# account selection
# view balance
# deposit
# withdraw
# logout

customers = [
  {
    "first_name": "Diana",
    "last_name": "Wilson",
    # "account_number": "4857291034",
    "account_number": "1234",
    "pin": "7302",
    "accounts": {
      "checking": 1245.91,
      "savings": 15602.87
    }
  }
]

class ATM:
    def __init__(self, card_inserted, user_pin):
        self.card_inserted = card_inserted
        self.user_pin = user_pin

    def login(self, card_inserted, user_pin):
        if card_inserted == False:
            return "Trouble reading bank card, please re-insert"
        else:
            user_account = input("Please enter your account number: ")

        for customer in customers:
            if user_account == customer["account_number"]:
                print("in the account loop")
                # account_pin = 7302
                if customer["pin"] == str(user_pin):
                    print("in the pin loop")
                    user_selects = ATM.display_menu()
                    return user_selects
                else:
                    return "Your PIN is wrong, try again."
            else:
                return "No account found. Please check the account number or visit the bank to open an account."
        
    def display_menu():
        print("\n**Welcome to the ATM**")
        print("1. Check Balance")
        print("2. Deposit Money")
        print("3. Withdraw Money")
        print("4. Exit")
        user_choice = input("Please choose an option from the menu (1-4): ").lower()

        user_options = {
            "1": (CheckBalance, "get_balance()"),
            "2": (DepositWithdraw, "add_deposit"),
            "3": (DepositWithdraw, "subtract_withdrawl"),
        }

        if user_choice in user_options:
            selected_class, method_name = user_options[user_choice]
            print(selected_class, method_name)
            instance = selected_class() # create instance of chosen class
            method_to_call = getattr(instance, method_name) # get the method from that instance
            method_to_call()
        else:
            print("Invalid Choice")

        return

login_checker = ATM(False, 7302)

# user_login = login_checker.login(True, 7302)
user_login = login_checker.login(True, 7302)

# class Users:
    
#     def __init__(self, account_number, pin, card_inserted):
#         self.__account_number  = account_number
#         self.__pin = pin
#         self.card_inserted = card_inserted

#     def user_check(self, card_inserted = True):
#         if self.card_inserted:
#             for k, v in accounts.items():
#                 print(k,v)

class CheckBalance:

    
    def __init__(self, account):
        self.account = account

    def get_balance(self, account):
        print("in the get balance method")
    #     if account == "checking":
    #         current_balance = customers[0]["accounts"]["checking"]
    #         return (f"Your current checking balance is {current_balance}")
    #     else:
    #         current_balance = customers[0]["accounts"]["savings"]
    #         return (f"Your current savings balance is {current_balance}")

# account_checker = CheckBalance("checking")

# check_balance = account_checker.get_balance("checking")
# check_balance = account_checker.get_balance("savings")
# # checkbalance = CheckBalance("savings")

# # print(current_account)
# # print(updated_balance)
# # print(checkbalance)
# print(check_balance)

class DepositWithdraw:
    pass
    
#     def __init__(self, deposit_amount, account, current_balance):
#         self.deposit_amount = deposit_amount
#         self.account = account
#         self.current_balance = current_balance

#     def add_deposit(self, current_balance, deposit_amount):
#         return current_balance + deposit_amount

#     def subtract_deposit(self, withdraw_amount):
#         # check if balance is hight enough to no overdrafting account
#         pass



# class ChooseAccount:
#     pass


# print(Users.user_check(True))
# print(current_account)
# print(updated_balance)