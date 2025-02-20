from test import BankAccount


class CheckingAccount(BankAccount):

    def __init__(self, customer_name, current_balance, remaining_balance, account_number, routing_number,minimum_balance = 50, daily_transfer_limit = 1000):
        super().__init__(customer_name, current_balance, remaining_balance, account_number, routing_number, minimum_balance)
        self.daily_transfer_limit = daily_transfer_limit
        self.transfer_count = 0

    def transfer(self, amount, target_account):

        if amount > self.daily_transfer_limit:
            print(f"Transfer exceeds daily limit of ${self.daily_transfer_limit}")
            return False

        if not self.withdraw(amount):  # Withdraw already checks for sufficient balance
            return False

        else:
            target_account.deposit(amount)
            self.transfer_count += 1
            print(f"Transfer successful: ${amount:.2f} sent to {target_account.customer_name}")
        return True

