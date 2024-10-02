# Qns. 4
# WITI Academy is proposing a sacco to help students save their money.
# Design a platform that will do the following.
# Welcome to, WITI Sacco
# deposit Money
# Withdraw Money 
# check Balance
# Ensure if the student selected 1, money is deposited and the minimum deposited should be 1000.
# if the student selects 2, money should be withdrawn and the minimum withdraw is 500.
# if the student selects 3, the account balance shold be displyed.


company = 'welcome to Witi Sacco'
diposit_money = 1000
withdraw_money = 500
check_balance = 'Balance'
class WITIAcademySacco:
    def __init__(self):
        self.balance = 0

        def deposit(self, amount):
            if amount >= 1000:
                self.balance +=
 amount
                print(f'successfully deposited{amount}. New balance is {self.balance}')
            else:
                 print('minimum')

