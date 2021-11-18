import random
from game import constants
from game.point import Point

class Actor:
    def __init__(self):
        """The class constructor."""
        self._position = Point(0, 0)
        self._velocity = Point(0, 0)
        self._text = ""
        self._x = 0
        self._y = 0

    def get_position(self):
        """Gets the actor's position in 2d space.
        
        Returns:
            Point: The actor's position in 2d space.
        """
        return self._position

    def get_text(self):
        """Gets the actor's textual representation.
        
        Returns:
            string: The actor's textual representation.
        """
        return self._text

    def get_velocity(self):
        """Gets the actor's speed and direction.
        
        Returns:
            Point: The actor's speed and direction.
        """
        return self._velocity

    def set_position(self, position):
        """Updates the actor's position to the given one.
        
        Args:
            position (Point): The given position.
        """
        self._position = position

    def set_text(self, text):
        """Updates the actor's text to the given value.
        
        Args:
            text (string): The given value.
        """
        self._text = text

    def set_velocity(self, velocity):
        """Updates the actor's velocity to the given one.
        
        Args:
            position (Point): The given velocity.
        """
        self._velocity = velocity

    def reverse_x(self):
        x = self._x * -1
        y = self._y
        return Point(x, y)

    def reverse_y(self):
        x = self._x
        y = self._y * -1
        return Point(x, y)

    def reverse_paddle_y(self):
        x = random.randint(1, 3)
        y = self._y * -1
        return Point(x, y)