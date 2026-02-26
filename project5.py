import turtle, math, time, random
from utils import *

# Section 1: Setup
# TODO - create your player character and any other sprites
# TODO - set your background
# TODO - set the starting value for your variables

who_is_it = "coolguydrizzy"
drake_tags = 0
future_tags = 0

sprite_list = []
t1 = create_sprite("coolguydrizzy",275,10)
t2 = create_sprite("future",-275,-50)

set_background("loakey")


# Section 2: Controls
# TODO - define your controls
# TODO - pick keys for each control
def move_up_1():
    x = t1.xcor()
    y = t1.ycor() + 10
    t1.goto(x,y)

window.onkeypress(move_up_1, "w")

def move_up_2():
    x = t2.xcor()
    y = t2.ycor() + 10
    t2.goto(x,y)

window.onkeypress(move_up_2, "Up")

def move_down_1():
    x = t1.xcor()
    y = t1.ycor() - 10
    t1.goto(x,y)

window.onkeypress(move_down_1, "s")

def move_down_2():
    x = t2.xcor()
    y = t2.ycor() - 10
    t2.goto(x,y)

window.onkeypress(move_down_2, "Down")

def move_left_1():
    x = t1.xcor()- 10
    y = t1.ycor() 
    t1.goto(x,y)

window.onkeypress(move_left_1, "a")

def move_left_2():
    x = t2.xcor() - 10
    y = t2.ycor() 
    t2.goto(x,y)

window.onkeypress(move_left_2, "Left")

def move_right_1():
    x = t1.xcor() + 10
    y = t1.ycor() 
    t1.goto(x,y)

window.onkeypress(move_right_1, "d")

def move_right_2():
    x = t2.xcor() + 10
    y = t2.ycor() 
    t2.goto(x,y)

window.onkeypress(move_right_2, "Right")

message1 = create_sprite("alien",-200,200)
message2 = create_sprite("alien",200,-200)


message1.goto(-220,220)
message2.goto(-150,-220)

# Section 3: Game Loop
window.listen()
for i in range(10000000000):
    if get_distance(t1, t2) < 150:
        if who_is_it== "coolguydrizzy":
            drake_tags =+ 1
            who_is_it = "future"
            t1.goto(275,10)
            t2.goto(-275,-50)

        elif who_is_it == "future":
            future_tags += 1
            who_is_it = "coolguydrizzy"

    if i >= 30 * 100:
        break

    # TODO - add code for automatic actions
    
    message1.color("white")
    message1.write("Drake Tags:",font = ("Arial", 40, "normal"))
    message1.hideturtle()


    message2.color("white")
    message2.write("Future Tags:",font = ("Arial", 40, "normal"))
    message2.hideturtle()




    # TODO - make an if statement for ending the game

    
    time.sleep(0.01)
    window.update()
    


print("Game Over")