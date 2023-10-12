import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.listen()


user = Player()
screen.onkey(user.move_player, "Up")
car_manager = CarManager()
scoreboard = Scoreboard()

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car_manager.create_cars()
    car_manager.move_cars()

    # detect collision with the cars
    for car in car_manager.all_cars:
        if car.distance(user) < 20:
            scoreboard.game_over()
            game_is_on = False

    # detect if user has reach other side
    if user.is_at_finish_line():
        scoreboard.increase_level()
        scoreboard.update_scoreboard()
        user.go_to_start()

screen.exitonclick()


