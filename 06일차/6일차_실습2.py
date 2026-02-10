class Account:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance
    
    def deposit(self, amount):
        self.balance += amount
    
    def withdraw(self, amount):
        self.balance -= amount
        
    def __str__(self):
        return f"소유자: {self.owner} / 잔액: {int(self.balance):,.0f}원"


class SavingsAccount(Account):
    def __init__(self, owner, balance, interest_rate):
        super().__init__(owner, balance)
        # self.owner = owner
        # self.balance = balance
        self.interest_rate = interest_rate
        
    def apply_interest(self):
        self.balance *= (1 + self.interest_rate)


class CheckingAccount(Account):
    def __init__(self, owner, balance, limit):
        super().__init__(owner, balance)
        self.limit = limit
        
    def withdraw(self, amount):
        if self.balance - amount < self.limit:
            print("최소 금액 초과하는 출금입니다. 다시 시도하세요.")
        else:
            self.balance -= amount
            
Minsuh = SavingsAccount("Minsuh", 100000, 0.05)
Jihoon = CheckingAccount("Jihoon", 50000, 30000)

print(Minsuh)
print(Jihoon)

Minsuh.deposit(20000)   # balance = 120000
Minsuh.apply_interest() # balance = 126000
print(Minsuh)

Jihoon.withdraw(70000)  # limit 초과
print(Jihoon)       # balance = 50000
Jihoon.withdraw(15000)  # balance = 35000
print(Jihoon)