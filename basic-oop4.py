class BankAccount():
    def __init__(self,name,age,amount):
        self.name = name
        self._age = age
        self.__amount = amount

    def showMessage(self):
        print('....')

    def _deposit(self,deposit):
        self._deposit += deposit
        print(f'Deposit..{deposit}..Balance..{self.__amount}')

    @property
    def amounts(self):
        return self.__amount
    
    @amounts.setter
    def amounts(self,amount):
        self.__amount = amount

    def __withdraw(self,withdraw):
        self.__withdraw += withdraw
        print(f'Withdraw..{withdraw}..Balance..{self.__amount}')

    # data = property(getAmount,setAmount)

class Employee(BankAccount):
    def __init__(self,name,age,amount):
        super().__init__(name,age,amount)

if __name__ == '__main__':
    employee = BankAccount('Vii', 30, 5555)

    print(employee.name)
    print(employee._age)
    print(employee.amounts)

    employee.amounts = 30
    print(employee.amounts)
    


