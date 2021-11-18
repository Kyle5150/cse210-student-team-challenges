from game import constants
from game.action import Action

class HandleCollisionsAction(Action):

    def execute(self, cast):

        cast["brick"] = []
        paddle = cast["paddle"][0] # there's only one
        ball = cast["ball"][0] # there's only one
        paddle_position = paddle.get_position()
        ball_position = ball.get_position()

        if ball_position.get_x() >= constants.MAX_Y -1:
            new_velocity = ball.get_velocity().reverse_y()
            ball.set_velocity(new_velocity)

        if ball_position.get_x() <= 0:
            new_velocity = ball.get_velocity().reverse_y()
            ball.set_velocity(new_velocity)

        for b in cast["brick"]:
            if ball_position.equals(cast["brick"].get_position()):
                new_velocity = ball.get_velocity().reverse_y()
                ball.set_velocity(new_velocity)
                cast["brick"].remove(cast["brick"].get_position())

        if paddle_position.get_y() - 1 == ball_position.get_y():
            min_x = paddle_position.get_x()
            max_x = min_x + len(paddle.get_text())
            if ball_position.get_x() >= min_x and ball_position.get_x() <= max_x:
                new_velocity = ball.get_velocity().reverse_paddle_y()
                ball.set_velocity(new_velocity)