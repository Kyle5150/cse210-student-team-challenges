import sys
from game.point import Point
from asciimatics.event import KeyboardEvent

class InputService:

    def __init__(self, screen):
        self._screen = screen
        self._keys = {}
        self._keys[97] = Point(-5, 0) # a97
        self._keys[100] = Point(5, 0) # d100
    
    def get_direction(self):
        """Gets the selected direction for the given player.
        Returns:
            Point: The selected direction.
        """
        direction = Point(0, 0)
        event = self._screen.get_event()
        if isinstance(event, KeyboardEvent):
            if event.key_code == 27:
                sys.exit()
            direction = self._keys.get(event.key_code, Point(0, 0))
        return direction