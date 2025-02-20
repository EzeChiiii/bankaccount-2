class BankAccount:
# Class attribute
    bank_title = "Chase"

# class SavingsAccount(BankAccount):
#     def interest_rate(self, customer_name, current_balance, remaining_balance, minimum_balance = 50, interest_rate = 1.5):
#
#         self.customer_name = customer_name
#         self.current_balance = current_balance
#         self.remaining_balance = remaining_balance
#         self.minimum_balance = minimum_balance
#         self.interest_rate = interest_rate
#
# class CheckingAccount(BankAccount):
#     def transfer_limitation(self):
#         pass


# Constructor method that holds parameters and has values assigned to each one
    def __init__(self, customer_name, current_balance, remaining_balance, account_number, routing_number, minimum_balance = 50):
        self.customer_name = customer_name
        self.current_balance = current_balance
        self.remaining_balance = remaining_balance
        self._account_number = account_number
        self.__routing_number = routing_number
        self.minimum_balance = minimum_balance

    # Calling the private routing number variable method
    def get_routing_number(self):
        return self.__routing_number



# Deposit method use to deposit money into bank account
    def  deposit(self, amount):
        if amount > 0:
            self.current_balance += amount
            self.remaining_balance += amount
            print(f"Your deposit was successful and your balance is: {self.current_balance}")
            print(f"Your remaining balance is: {self.remaining_balance}")
        else:
            print("Amount has to be greater than 0")

# Withdraw method used to withdraw money out of bank account
    def withdraw(self, amount):
        if amount <= 0:
            print("Amount has to be greater than 0")
            return False
        elif  self.remaining_balance - amount < self.minimum_balance:
            print(f"Your remaining balance will go below the minimum balance of {self.minimum_balance}")
            return False
        else:
            self.current_balance -= amount
            self.remaining_balance -=amount
            print(f"{self.customer_name} your withdrawal of {amount} was successful")
            print(f"Remaining balance: {self.remaining_balance}")
            return True

# Method that holds the account owner's information
    def customer_info(self):
        print("\nCustomer Info: ")
        print(f"Bank: {BankAccount.bank_title}")
        print(f"Customer Name: {self.customer_name}")
        print(f"Account Number: {self._account_number}")
        print(f"Routing Number: {self.get_routing_number()}")
        # print(f"Minimum Balance: {self.minimum_balance}")
        print(f"Current Balance: {self.current_balance}")
        print(f"Remaining Balance: {self.remaining_balance}")
        print("_________\n")



# Bank account instance of the Object created
account_user = BankAccount("Clinton Iwu", 1000, 1000, 456778888,766554445)

# account_user.withdraw(100)
# account_user.deposit(1000)
#
# print(account_user.customer_info())
#
# user_two = BankAccount("Angel Ware", 500, 500)
# user_two.customer_info()
# user_two.deposit(10000)
# user_two.withdraw(900)
# print(user_two.customer_info())



