class A:
    @staticmethod
    def method():
        print('ASD')
    # method = staticmethod(method)


class Account:
    def __init__(self, owner, account_number, account_balance, max_daily_turnover=1500):
        self.owner = owner
        self.account_number = account_number
        self.account_balance = account_balance
        self.max_daily_turnover = max_daily_turnover
        self.turnover_today = 0

    def money_transfer(self, destination, amount):

        # here the test place whether the transfer is possible
        if amount < 0 or (self.turnover_today + amount > self.max_daily_turnover
                          or destination.turnover_today + amount > destination.max_daily_turnover):
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

    # def junior_account( owner, account_number, account_balance):
    #     return Account(owner,account_number, account_balance, 20)
    # junior_account = staticmethod(junior_account)
    @staticmethod
    def junior_account(owner, account_number, account_balance):
        return Account(owner, account_number, account_balance, 20)

    def show(self):
        # print(("Account of {}".format(self.owner)))
        # print("Current account balance: {:.2f} Euro".format(self.account_balance))
        # print("Today already {:2f} of {} Euro turned over".format(self.turnover_today, self.max_daily_turnover))
        print(f"Account of {self.owner}")
        print(f"Current account balance: {self.account_balance:.2f} Euro")
        print(f"Today already {self.turnover_today:.2f} of {self.max_daily_turnover} Euro turned over")


# ======= executing  ==========

# jr = Account.junior_account("Ethan Peters", 436574, 67)

jr = Account("Ethan Peters", 436574, 67)

jr.junior_account("Ethan Peters", 436574, 97) # have not error, but don't change max_daily_turnover and account_balance

jr.show()
jr.deposit(20)
jr.show()
jr.deposit(10)
jr.show()

A.method()
a = A()
a.method()  # TypeError: A.method() takes 0 positional arguments but 1 was given
