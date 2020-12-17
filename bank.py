global trans


class Customer:
    last_id = 0

    def __init__(self, first_name, last_name, email):
        Customer.last_id += 1
        self.customer_id = Customer.last_id
        self.first_name = first_name
        self.last_name = last_name
        self.email = email

    def __str__(self):
        return "Customer[{0},{1},{2}]".format(self.customer_id, self.first_name, self.last_name)


class Account:
    last_id = 0
    interest_rate = 0.02

    def __init__(self, customer):
        Account.last_id += 1
        self.account_id = Account.last_id
        self.customer = customer
        self._balance = 0
        self.history = {}

    def deposit(self, amount):
        self._balance = self._balance + amount
        if (self.history.has_key('Credit')):
            self.history['Credit'].append(amount)
        else:
            self.history['Credit'] = ([amount])

    def charge(self, amount):
        if amount > self._balance:
            raise BankException('Not enough money')
            # return -1
        self._balance = self._balance - amount
        if (self.history.has_key('Debit')):
            self.history['Debit'].append(amount)
        else:
            self.history['Debit'] = ([amount])
        return 0

    def calc_interest(self):
        self._balance = self._balance + self.calc_interest_value(self._balance)
        if (self.history.has_key('Interest')):
            self.history['Interest'].append(self._balance)
        else:
            self.history['Interest'] = ([self._balance])
        return 0

    @classmethod
    def calc_interest_value(cls, amount):
        return cls.interest_rate * amount

    def get_balance(self):
        return self._balance

    def __str__(self):
        return "{3}[{0},{1},{2}]".format(self.account_id, self._balance, self.customer.last_name,
                                         self.__class__.__name__)


class SavingsAccount(Account):
    interest_rate = 0.03


class DebitAccount(Account):
    interest_rate = 0.001


class BankException(Exception):
    pass


c1 = Customer('Anne', 'Smith', 'anne@smith.com')
c2 = Customer('John', 'Brown', 'john@smith.com')
print(c1)
# a1 = SavingsAccount(c1)
a1 = DebitAccount(c1)
print(a1)
a1.deposit(2000)
a1.charge(1200)
a1.calc_interest()
a1.deposit(300)
a1.charge(100)
a1.calc_interest()
# a2 = SavingsAccount(c2)
a2 = DebitAccount(c2)
print(a2)
a2.deposit(1200)
a2.calc_interest()
a2.charge(100)
a2.deposit(300)
a2.charge(800)
a2.calc_interest()
s = str(a1)
print(a1.get_balance())

print("History of transaction of Anne Smith")
print(a1.history)

print("History of transaction of John Brown")
print(a2.history)

print("Current Status of Anne Smith")

print(a1)

print("Current Status of John Brown")

print(a2)