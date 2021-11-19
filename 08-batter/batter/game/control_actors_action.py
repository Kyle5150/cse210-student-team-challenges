from game import constants
# from game.action import Action
from game.actor import Actor

class ControlActorsAction(Actor):
    def __init__(self, input_service, actor):
        """The class constructor.
        
        Args:
            input_service (InputService): An instance of InputService.
        """
        self._input_service = input_service
        self._actor = actor
    
    def execute(self, cast):
        """Executes the action using the given actors.
        Args:
            cast (dict): The game actors {key: tag, value: list}.
        """
        velocity = self._actor.get_velocity()
        direction = self._input_service.get_direction()
        paddle = cast["paddle"][0] # there's only one in the cast
        paddle.set_velocity(direction)
        ball = cast["ball"][0]
        ball.set_velocity(velocity)
        # bricks = cast["brick"][0]