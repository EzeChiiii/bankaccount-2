from savings import Savings
from checking import CheckingAccount

# Creating Savings Accounts
mike_savings = Savings("Mike",2000,2000,383948338,838493039, interest_rate = 2.5)
melissa_saving = Savings("Melissa",1000,1000,38394838,838493372, interest_rate = 3.0)

print("=== New Savings Accounts ===")

mike_savings.customer_info()
mike_savings.deposit(1000)
mike_savings.apply_interest()
mike_savings.customer_info()

melissa_saving.customer_info()
melissa_saving.withdraw(200)
melissa_saving.apply_interest()
melissa_saving.customer_info()

print("=== New Checking Accounts ===")

brian_checking = CheckingAccount("Brian", 200, 200, 83292929, 73748848)
michael_checking = CheckingAccount("Michael", 1000, 1000, 83564929, 73713448)
thomas_checking = CheckingAccount("Thomas", 1200, 1200, 83276529, 73787948)
chris_checking = CheckingAccount("Chris", 900, 900, 89872929, 73787748)

print(thomas_checking.customer_info())
brian_checking.customer_info()
brian_checking.withdraw(20)
brian_checking.transfer(50, thomas_checking)
print(brian_checking.customer_info())
print(thomas_checking.customer_info())


print(chris_checking.customer_info())
michael_checking.customer_info()
michael_checking.withdraw(20)
michael_checking.transfer(500, chris_checking)
print(michael_checking.customer_info())
print(chris_checking.customer_info())






# print(michael_checking.customer_info())
# print(thomas_checking.customer_info())
# print(chris_checking.customer_info())


# thomas_checking.customer_info()
# thomas_checking.transfer(1000, michael_checking)
# thomas_checking.customer_info()
#
# chris_checking.customer_info()
# chris_checking.transfer(500, michael_checking)





