class One():
    def __init__(self,menu,favour,unit,price):
        self.menu = menu
        self.favour = favour
        self.unit = unit
        self.price = price

    def buy(self):
        if self.unit >= '5' :
            print('Thank you')
        else :
            print('......')

    def tasty(self):
        if self.favour == 'very sweet':
            print(f'this is my {self.favour} : It is not for health')
        else:
            print('It is very tasty')

class Two(One):
    def __init__(self,name,favour,unit,price):
        super().__init__(name,favour,unit,price)
        self.price = price

    def pay(self):
        print(f'I must to pay {self.price}')

if __name__ == '__main__':
    one1 = One('papa','spicy','7','80')
    two1 = Two('pimpim','very sweet','3','50')

    print(one1.favour)
    one1.buy()

    print(two1.favour)
    two1.tasty()
