import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

SLEEP_TIMER = 0.1
game_is_on = True

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.listen()
player = Player()
car_manager = CarManager()
screen.onkeypress(key='Up',fun=player.move_forward)


while game_is_on:
    time.sleep(SLEEP_TIMER)
    screen.update()
    car_manager.create_car()
    car_manager.move_cars()

    #Detect collision with car
    for car in car_manager.all_cars:
        if car.distance(player) < 20:
            game_is_on = False
    turtle_ycor = player.ycor()
    if turtle_ycor >= 280:
        player.go_to_start()
        car_manager.leve_up()


screen.exitonclick()
