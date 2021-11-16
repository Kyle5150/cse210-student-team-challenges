class InputService:
    pass

    def __init__(self, screen):
        self._screen = screen
        self._keys = {}
        self._keys[97] = Point(-5, 0) # a
        self._keys[100] = Point(5, 0) # d
    
    