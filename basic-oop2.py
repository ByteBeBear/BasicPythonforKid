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
            print(f'This favour is {self.favour} : It is not for health')
        else:
            print('It is very tasty')

class Two(One):
    def __init__(self,name,favour,unit,price):
        super().__init__(name,favour,unit,price)
        self.price = price

    def pay(self):
        print(f'I must to pay {self.price}')

    def discount(self):
        if self.unit >= "10":
            print('..Free 1..')
        else:
            print('Thank you')

if __name__ == '__main__':
    one1 = One('Mummee','spicy','7','80')
    two1 = Two('Lyuda','very sweet','10','50')

    print(one1.favour)
    one1.buy()
    print(f'I want {two1.unit} pieces ')
    two1.discount()

    print(two1.favour)
    two1.tasty()

    
