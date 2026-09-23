import snake_game


def test_game_constants():
    assert snake_game.GAME_WIDTH == 700
    assert snake_game.GAME_HEIGHT == 700
    assert snake_game.SPEED == 100
    assert snake_game.SPACE_SIZE == 20
    assert snake_game.BODY_PARTS == 3


def test_snake_color():
    assert snake_game.SNAKE_COLOR == "#00FF00"


def test_food_color():
    assert snake_game.FOOD_COLOR == "#FF0000"


def test_background_color():
    assert snake_game.BACKGROUND_COLOR == "#000000"


def test_change_direction():
    snake_game.direction = "down"

    snake_game.change_direction("left")
    assert snake_game.direction == "left"

    snake_game.change_direction("up")
    assert snake_game.direction == "up"

    snake_game.change_direction("right")
    assert snake_game.direction == "right"


def test_prevent_reverse_direction():
    snake_game.direction = "down"

    snake_game.change_direction("up")

    assert snake_game.direction == "down"


def test_wall_collision():
    snake = type("Snake", (), {})()
    snake.coordinates = [[-20, 0]]

    assert snake_game.check_collisions(snake) is True


def test_no_collision():
    snake = type("Snake", (), {})()
    snake.coordinates = [[100, 100]]

    assert snake_game.check_collisions(snake) is False


def test_self_collision():
    snake = type("Snake", (), {})()
    snake.coordinates = [
        [100, 100],
        [80, 100],
        [100, 100]
    ]

    assert snake_game.check_collisions(snake) is True
