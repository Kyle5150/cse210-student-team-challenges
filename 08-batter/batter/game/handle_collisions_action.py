import random
from game import constants
# from game.action import Action
from game.actor import Actor
from game.point import Point
from game.director import Director
import sys
import os

class HandleCollisionsAction(Actor):

    def execute(self, cast):
        
        # self.keep_playing = True
        bricks = cast["brick"]
        paddle = cast["paddle"][0] # there's only one
        ball = cast["ball"][0] # there's only one
        paddle_position = paddle.get_position()
        ball_position = ball.get_position()

        # #ball/brick collision method 1
        for brick in bricks:
            brick_hitbox = []
            for i in range(0, 2, 1): #brick size 2
                brick_piece = Point((brick.get_position().get_x() + i), brick.get_position().get_y())
                brick_hitbox.append(brick_piece)

            for hitbox_component in brick_hitbox:
                if ball.get_position().equals(hitbox_component):
                    # velocity = ball.get_velocity().reverse()
                    velocity = Point(random.randint(-1, 1), ball.get_velocity().reverse().get_y())
                    ball.set_velocity(velocity)
                    brick.set_text("")
                    brick.set_position(Point(0, 0))

                    # score.add_points(1)

        if ball_position.get_x() >= constants.MAX_X -1 or ball_position.get_x() <= 0 +1:
            new_velocity = ball.get_velocity().reverse_x()
            ball.set_velocity(new_velocity)

        if ball_position.get_y() <= 0 +1:
            new_velocity = ball.get_velocity().reverse_y()
            ball.set_velocity(new_velocity)

        if ball_position.get_y() >= constants.MAX_Y -1:
            os.system("clear")
            print("GAME OVER")
            sys.exit()

        empty = True

        for hitbox_component in brick_hitbox:
            if brick.get_text() == "":
                continue
            else:
                empty = False
                break

        if empty == True:
            sys.exit()

        # ball/brick collision method 2
        # if ball_position.get_x() <= 0:
        #     new_velocity = ball.get_velocity().reverse()
        #     ball.set_velocity(new_velocity)

        # for brick in cast["brick"]:
        #     if ball_position.equals(cast["brick"].get_position()):
        #         new_velocity = ball.get_velocity().reverse()
        #         ball.set_velocity(new_velocity)
        #         cast["brick"].remove(cast["brick"].get_position())

        if paddle_position.get_y() - 1 == ball_position.get_y():
            min_x = paddle_position.get_x()
            max_x = min_x + len(paddle.get_text())
            if ball_position.get_x() >= min_x and ball_position.get_x() <= max_x:
                new_velocity = ball.get_velocity().reverse_paddle_y()
                ball.set_velocity(new_velocity)

        if paddle_position.get_x() == 0:
            paddle_position = paddle_position

        if paddle_position.get_x() == 80:
            paddle_position = paddle_position