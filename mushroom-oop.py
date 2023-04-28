class Order():
    name = None
    color = None
    flavour = None
    size = None

    def __init__(self,name,detail,flavour,size):
        self.name = name
        self.detail = detail
        self.flavour = flavour
        self.size = size

    def eat(self):
        print(f'I would like to eat {self.flavour} flavour.')

    

class Menu():
    def eat(self):
        print(f'I wanna buy {self.size}')

if __name__ == '__main__':

    name1 = Order('Mushroomcurry','grilled with curry sauce','hot','Mini')
    name2 = Order('Shrimpdong','pickled with Korea soy sauce','spicy ','SetCombo')

    print(f'I want to order {name2.name}.')
    print(f'and {name2.detail}')

    print(f'I choose {name1.flavour}.')
    name1.eat()
    
    print(f'I choose {name2.size}.')
    name2.eat()