def pin_authentication(pin):
    if pin == '1234':
        return True
    else:
        return False


def _log_in():
    pin = input('Please Enter Your 4 Digit Pin: ')
    if pin_authentication(pin):
        print("Pin correct")
        return True
    else:
        print("Invalid pin")


class Account:
    def __init__(self):
        self.balance = 1000000

    def _withdraw(self, amount):
        self.balance = self.balance - amount
        print("Account balance is: ", self.balance)


class SavingsAccount(Account):
    def __init__(self):
        Account.__init__(self)

    def savingsWithdraw(self, amount):
        if (amount < 100000):
            super()._withdraw(amount)
        else:
            print("Amount exceeds withdrawal limit")


class CurrentAccount(Account):
    def __init__(self):
        Account.__init__(self)

    def currentWithdraw(self, amount):
        # depends on the balance
        super()._withdraw(amount)
        if (self.balance > 100000):
            pass
        else:
            print("Account Balance limit reached")


if _log_in():
    choice = int(input('Press 1 for Savings account and 2 for Current account: '))
    if choice == 1:
        amount = int(input("Enter amount:  "))
        savings = SavingsAccount()
        savings.savingsWithdraw(amount)
    elif choice == 2:
        amount = int(input("Enter Amount: "))
        current = CurrentAccount()
        current.currentWithdraw(amount)
    else:
        print("invalid choice")
