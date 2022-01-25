from abc import ABC, abstractmethod

class Shape (ABC):
    def __init__ (self, area, perimeter):
        self.area = area
        self.perimeter = perimeter

@property
@abstractmethod
def s (self):
    pass

class Rect (Shape):
    class Line:
        class Point:
            def __init__ (self, x, y):
                self.x = x
                self.y = y
        def __init__ (self, length, x, y):
            self.length = length
            length = float (y - x)
            print ('Line is: ' , length)
    @property
    def s (self):
        print (f'The area of the square is {self.area} and the perimeter is {self.perimeter}')

    class Square (Shape, Line):
        @property 
        def s (self):
            print (f'The area of the square is {self.area} and the perimeter is {self.perimeter}')

    class Cube (Square):
        def __init__ (self, volume, length):
            self.volume = volume
            volume = float (length ** 3)
            print ('The volume of the cube: ', volume)



