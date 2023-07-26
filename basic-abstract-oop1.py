class Square:
    def __init__(self, length):
        self.length = length

    def calculate(self):
        return self.length

class Cube(Square):
    def __init__(self, length):
        super().__init__(length)

    def calculate(self):
        return super().calculate()
    
if __name__ == '__main__':
    square = Square(1)
    print(f'..SquareArea = {square.calculate()}..')

    cube = Cube(111)
    print(f'..CubicVolume = {cube.calculate()} table.')