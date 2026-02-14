#Super function used in a child class to call methods from a parent class(superclass)

class Shape:
    def __init__(self,color,is_filled):
        self.color = color
        self.is_filled = is_filled
        

class Circle(Shape):
    def __init__(self,color,is_filled,radius):
        super().__init__(color,is_filled)
        self.radius=radius

class Square(Shape):
    def __init__(self,color,is_filled,side):
        super().__init__(color,is_filled)
        self.side=side

circle1 = Circle("blue",True,45)

print(circle1.color)





        

        





    