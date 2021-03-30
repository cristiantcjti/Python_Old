class Account:
    
    def __init__(self, number, holder, balance, limit,):
        self.__number = number
        self.__holder = holder
        self.__balance = balance
        self.__limit = limit

    def statement(self):
        print(f"The statement account of {self.__holder} is {self.__balance}!")

    def deposit(self, value):
        self.__balance += value

    def __allow_withdraw(self, value_withdraw):
        value_allowed = self.__balance + self.__limit
        return value_withdraw <= value_allowed
    
    def withdraw(self, value):
        if (self.__allow_withdraw(value)):
            self.__balance -= value
        else:
            print(f"The value to withdraw is not allowed. This is the limit: {self.__limit+self.__balance}")
    
    def transfer(self, value, target_account):
        self.withdraw(value)
        target_account.deposit(value)
    @property    
    def balance(self):
        return self.__balance

    @property
    def holder(self):
        return self.__holder

    @property               #It allows to call the method: object.limit
    def limit(self):
        return self.__limit
    
    @limit.setter           #It allows to set a value: object.limit = 5000.0
    def limit(self, limit):
        self.__limit = limit

    @staticmethod
    def bank_codes():
        return {'BB':'001', 'Caixa':'104', 'Bradesco':'237'}
    


