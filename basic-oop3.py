class One():
    def __init__(self,brand,version,color,year):
        self.brand = brand
        self.version = version
        self.color = color
        self.year = year
    
    def drive(self):
        print(f'I am interested {self.brand}.and {self.color} color.')

    def buy(self):
        print(f'I wounld like to buy {self.brand} {self.version} {self.year}.')

class Two(One):
    def __init__(self,brand,version,color,year,price):
        super().__init__(brand,version,color,year)
        self.price = price

    def change(self):
        if self.price <= '7000000':
            print('___Thank you and I have give away for you___')
        else:
            print('...Thank you...')

if __name__ == '__main__':
    one1 = One('Porche','Taycan','pink','2021')
    two1 = Two('Porche','Cayenne','black','2022','7000000')

    one1.drive()
    one1.buy()
    two1.change()