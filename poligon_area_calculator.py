import re

class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def __str__(self):
        return f'{self.__class__.__name__}(width={self.width}, height={self.height})'

    def set_width(self, w):
        self.width = w

    def set_height(self, h):
        self.height = h
        
    def get_area(self):
        return self.width * self.height

    def get_perimeter(self):
        return 2 * self.width + 2 * self.height

    def get_diagonal(self):
        return (self.width**2 + self.height**2)**.5

    def get_picture(self):
        if self.width > 50 or self.height > 50:
            return 'Too big for picture.'
        else:
            picture = ''
            for p in range(self.height):
                picture += ('*'* self.width) + '\n'
            return picture
    
    def get_amount_inside(self, shape):
        shape = re.findall('\d+', str(shape))

        try:
            shapeArea = int(shape[0]) * int(shape[1])
        except IndexError: 
            shapeArea = int(shape[0]) ** 2

        amountInside = self.get_area() // shapeArea
        if amountInside < 1:
            return 0
        else:
            return amountInside

class Square(Rectangle):
    def __init__(self, side):
        self.side = side
        self.width = side
        self.height = side
        
    def __str__(self):
        return f'{self.__class__.__name__}(side={self.side})'
        
    def set_side(self, s):
        self.side = s
        self.width = s
        self.height = s

    def set_width(self, width):
        self.side = width

    def set_height(self, height):
        self.side = height
        

       



