from abc import ABC, abstractmethod

class Rectanger(ABC):

    @abstractmethod
    def calculate(self):
        pass

class Rectangular(Rectanger):
    def __init__(self,width,length,depth):
        self.width = width
        self.length = length
        self.depth = depth
    
    def calculate(self):
        return self.width * self.length * self.depth   # return self.width คูณกัน
if __name__ == '__main__':
    rect3D = Rectangular(8 , 10 ,5)
    print(f'?? = {rect3D.calculate()} cm. ')