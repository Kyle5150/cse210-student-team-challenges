from game import constants
from game.action import Action

class ControlActorsAction(Action):
    def __init__(self, input_service):
        """The class constructor.
        
        Args:
            input_service (InputService): An instance of InputService.
        """
        self._input_service = input_service
    
    def execute(self, cast):
        """Executes the action using the given actors.
        Args:
            cast (dict): The game actors {key: tag, value: list}.
        """
        direction = self._input_service.get_direction()
        paddle = cast["paddle"][0] # there's only one in the cast
        paddle.set_velocity(direction)
        ball = cast["ball"][0]
        ball.set_velocity(direction)
        # bricks = cast["brick"][0]