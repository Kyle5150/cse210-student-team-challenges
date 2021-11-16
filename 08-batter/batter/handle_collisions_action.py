class HandleCollisionsAction(Actor):
    pass

    paddle = cast["paddle"][0]
    ball = cast["ball"][0]
    paddle_position = paddle.get_position()
    ball_position = ball.get_position()

    if ball_position.get_x() >= constants.MAX_Y -1:
        pass

    if ball_position.get_x() <= 0:
        pass



    bricks = cast["brick"]



    if paddle_position.get_y() - 1 == ball_position.get_y():
        min_x = paddle_position.get_x()
        max_x = min_x + len(paddle.get_text())
        if ball_position.get_x() >= min_x and ball_position.get_x() <= max_x:
            new_velocity = ball.get_velocity().reverse()
            ball.set_velocity(new_velocity)