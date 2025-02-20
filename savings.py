from test import BankAccount

class Savings(BankAccount):

        #Constructor
    def __init__(self, customer_name, current_balance, remaining_balance, account_number, routing_number, minimum_balance = 50, interest_rate = 1.5):

        super().__init__(customer_name, current_balance,  remaining_balance, account_number, routing_number,minimum_balance)

        self.interest_rate = interest_rate

    #method to apply interest on saving account instance
    def apply_interest(self):

        interest = round(self.current_balance * (self.interest_rate/100), 2)
        self.current_balance += interest
        self.remaining_balance += interest

        print(f"Interest applied: ${interest:.2f}")
        print(f"New balance: {self.current_balance}")
        return self.current_balance


    def display_routing_number(self):

        print(f"Savings Account Routing Number: {self.get_routing_number()}")

# user2 = Savings("Angel Ware", 500, 500, 434678890, 865468646)
# user2.customer_info()
# user2.apply_interest()
# print(user2.get_routing_number())














