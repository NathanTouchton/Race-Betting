from turtle import Turtle, Screen
from random import randint

screen = Screen()
screen.setup(width=500, height=400)

colors = ["red", "orange", "yellow", "green", "blue", "purple"]
y_positions = [-180, -120, -60, 0, 60, 120]
all_turtles = []

for turtle_index in range(0, 6):
    turtle = Turtle(shape="turtle")
    turtle.penup()
    turtle.color(colors[turtle_index])
    turtle.goto(x=-230, y=y_positions[turtle_index])
    all_turtles.append(turtle)

IS_RACE_ON = False

USER_BET = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")
if USER_BET:
    IS_RACE_ON = True

while IS_RACE_ON:
    for turtle in all_turtles:
        if turtle.xcor() > 230:
            IS_RACE_ON = False
            winning_color = turtle.pencolor()
            if winning_color == USER_BET:
                print(f"You've won! The {winning_color} turtle won!")
            else:
                print(f"You lose! The {winning_color} turtle won.")
        rand_distance = randint(0, 10)
        turtle.forward(rand_distance)

screen.exitonclick()
