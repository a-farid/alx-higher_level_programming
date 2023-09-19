#!/usr/bin/python3
'''MODULE CONTAININI THE RECTANGLE CLASS'''
from models.base import Base


class Rectangle(Base):
    '''The rectangle class'''

    def __init__(self, width, height, x=0, y=0, id=None):
        super().__init__(id)
        if not isinstance(width, int):
            raise TypeError('width must be an integer')
        if width <= 0:
            raise ValueError('width must be > 0')
        if not isinstance(height, int):
            raise TypeError('height must be an integer')
        if height <= 0:
            raise ValueError('height must be > 0')
        if not isinstance(x, int):
            raise TypeError('x must be an integer')
        if x < 0:
            raise ValueError('x must be >= 0')
        if not isinstance(y, int):
            raise TypeError('y must be an integer')
        if y < 0:
            raise ValueError('y must be >= 0')

        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

    @property
    def width(self):
        '''Set / Get the width of the rectangle'''
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError('width must be an integer')
        if value <= 0:
            raise ValueError('width must be > 0')
        self.__width = value

    @property
    def height(self):
        '''Set / Get the heigth of the rectangle'''
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError('height must be an integer')
        if value <= 0:
            raise ValueError('height must be > 0')
        self.__height = value

    @property
    def x(self):
        '''Set / Get the x value of the rectangle'''
        return self.__x

    @x.setter
    def x(self, value):
        if not isinstance(value, int):
            raise TypeError('x must be an integer')
        if value < 0:
            raise ValueError('x must be >= 0')
        self.__x = value

    @property
    def y(self):
        '''Set / Get the y value of the rectangle'''

        return self.__y

    @y.setter
    def y(self, value):
        if not isinstance(value, int):
            raise TypeError('y must be an integer')
        if value < 0:
            raise ValueError('y must be >= 0')
        self.__y = value

    def area(self):
        '''Return the area of the rectangle'''
        return self.__width * self.__height

    def display(self):
        '''Display the rectangle'''
        [print() for y in range(self.__y)]
        for h in range(self.__height):
            print(f'{" " * self.__x}{"#" * self.__width}')

    def __str__(self):
        """Return the print() and str() representation of the Rectangle."""
        return "[Rectangle] ({}) {}/{} - {}/{}".format(self.id,
                                                       self.x, self.y,
                                                       self.width, self.height)

    def update(self, *args, **kwargs):
        '''
        Update the values of the rectangle

        Args:
         *args (ints): New attribute values.
                - 1st argument represents id attribute
                - 2nd argument represents width attribute
                - 3rd argument represent height attribute
                - 4th argument represents x attribute
                - 5th argument represents y attribute
            **kwargs (dict): New key/value pairs of attributes.
        '''
        # Handling the update with the kwargs
        if 'id' in kwargs:
            self.id = kwargs['id'] or args[0]
        if 'width' in kwargs:
            self.__width = kwargs['width'] or args[1]
        if 'height' in kwargs:
            self.__height = kwargs['height'] or args[2]
        if 'x' in kwargs:
            self.__x = kwargs['x'] or args[3]
        if 'y' in kwargs:
            self.__y = kwargs['y'] or args[4]

        # Handling the update with the args
        if len(args) == 1:
            self.id = args[0]
        if len(args) == 2:
            self.__width = args[1]
        if len(args) == 3:
            self.__height = args[2]
        if len(args) == 4:
            self.__x = args[3]
        if len(args) == 5:
            self.__y = args[4]

    def to_dictionary(self):
        '''Return the dictionnary representation of the rectangle'''
        return {'x': self.__x,
                'y': self.__y,
                'id': self.id,
                'height': self.__height,
                'width': self.__width}

