


class Figure:
    def __init__(self, numberOfSides):
        self.count = numberOfSides
        self.sides = [0 for i in range(numberOfSides)]
    
    def inputSides(self):
        self.sides = [float(input()) for i in range(self.count)]

class Triangle(Figure):
    def __init__(self):
        Figure.__init__(self, 3)
    
    def findPerimeter(self):
        a, b, c = self.sides
        perimeter = a + b + c
        # print(perimeter)
        return perimeter

    def findArea(self):
        a, b, c = self.sides
        s = (a + b + c) / 2
        area = (s * (s - a) * (s - b) * (s - c))
        
        # print(area)
        return area ** 0.5
        


if __name__ == "__main__":
    triangle =  Triangle()

    triangle.inputSides()
    print(triangle.findPerimeter())
    print(triangle.findArea())
