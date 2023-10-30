

class Account:
    def __init__(self, owner, account_number, account_balance, max_daily_turnover=1500):
        self.owner = owner
        self.account_number = account_number
        self.account_balance = account_balance
        self.max_daily_turnover = max_daily_turnover
        self.turnover_today = 0
    def money_transfer(self, destination, amount):

        # here the test place whether the transfer is possible
        if amount < 0 or self.turnover_today + amount > self.max_daily_turnover or destination.turnover_today + amount > destination.max_daily_turnover:
            # transfer impossible
            return False
        else:
            # everything is OK - Let's go
            self.account_balance -= amount
            self.turnover_today += amount
            destination.account_balance += amount
            destination.turnover_today += amount
            return True

    def deposit(self, amount):
        if amount < 0 or self.turnover_today + amount > self.max_daily_turnover:
            # daily limit exceed or invalid amount
            return False
        else:
            self.account_balance += amount
            self.turnover_today += amount
            return True

    def withdraw(self, amount):
        if amount < 0 or self.turnover_today + amount > self.max_daily_turnover:
            # daily limit exceed or invalid amount
            return False
        else:
            self.account_balance -= amount
            self.turnover_today += amount
            return True

    def show(self):
        # print(("Account of {}".format(self.owner)))
        # print("Current account balance: {:.2f} Euro".format(self.account_balance))
        # print("Today already {:2f} of {} Euro turned over".format(self.turnover_today, self.max_daily_turnover))
        print(f"Account of {self.owner}")
        print(f"Current account balance: {self.account_balance:.2f} Euro")
        print(f"Today already {self.turnover_today:.2f} of {self.max_daily_turnover} Euro turned over")

    #======= executing  ==========

a1 = Account("Steve Miller", 567_123, 12_350.00)
a2 = Account("Jonh Smith", 396_754, 15_000.00)
a1.money_transfer(a2, 1_000)
a2.money_transfer(a1, 500)
a1.show()
a2.show()

"""Account of Steve Miller
Current account balance: 11850.00 Euro
Today already 1500.00 of 1500 Euro turned over
Account of Jonh Smith
Current account balance: 15500.00 Euro
Today already 1500.00 of 1500 Euro turned over"""
