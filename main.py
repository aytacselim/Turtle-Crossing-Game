import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard
from lines import Lines

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
car_list = []
for _ in range(10):
    new_car = CarManager()
    car_list.append(new_car)
scoreboard = Scoreboard()
lines = Lines()


screen.listen()
screen.onkeypress(player.go_up, "Up")
screen.onkeypress(player.go_left, "Left")
screen.onkeypress(player.go_right, "Right")
screen.onkeypress(player.go_down, "Down")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    if player.is_at_finish_line():
        player.reset_position()
        scoreboard.add_level()
        for car in car_list:
            car.level_up()
    for car in car_list:
        car.move()
        if player.distance(car) < 22.5:
            game_is_on = False
            scoreboard.game_over()
        if car.xcor() < -320:
            car.reset_position()

screen.exitonclick()
