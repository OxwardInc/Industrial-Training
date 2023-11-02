import random
from random import *
class Banking_application(self, name, dob, phone, address, email, deposit):
    self.name = name
    self.bvn = '02'
    for i in range(9):
        digit = random.randint(0, 9)
        self.bvn += str(digit)
    self.date_of_birth = dob
    self.phone_number = phone
    self.address = address
    self.email = email
    self.deposit == deposit
    self.account_type = 'Savings'
    self.acc_number = '05'
    for num in range(8):
        digit = random.randint(0, 9)
    self.balance = deposit

    def make_withdrawal(self, amount):
        if amount >= self.balance:
            return f"Insufficient fund's, your balance is {self.balance}"
        elif amount < self.balance:
            self.balance = self.balance - amount
            return f"Withdrawal of {amount} is succesful and your balance is {self.balance}"

    def upgrade_account_type(self, _type):
        if _type not in ['Current', 'Credit']:
            return 'Upgrade failed!'
        self.account_type = _type

    def make_deposit(sef, amount):
        if self.account_type == 'Savings':
            if amount > 10000:
                return f"You're not able to deposite more than $10,00 at once"
        elif self.account_type == 'Credit':
            if amount > 50000:
                return f"Your limit for this account type is $50,000 and what you're trying to deposit is {amount}"
        else:
            self.balance += amount

    def transfer_funds(self, acc_number, amount):
        acc_number = self.acc_number
        if amount <= self.balance:
            self.balance -= amount
            print(f'Transfer successful to {acc_number}')
        else:
            return 'Insuffucient balance'

