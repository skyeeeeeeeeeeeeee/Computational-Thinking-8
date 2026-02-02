import turtle, time, random
from utils import *

# Section 1 - setup
# TODO - set a background using 
set_background("sunset")

# TODO - create at least two variables and set their starting value. ex: cookies = 0
aura_points=0
moneycoins=10



# Section 2 - controls
# TODO - define an action. ex: def my_control()
def aura_points():
    global aura_points
    aura_points +=1

# TODO - choose a key to do the action. ex: window.onkeypress(my_control, "space")
window.onkeypress(aura_points, "space")

# TODO - make a second control
def get_your_money_up():
    global moneycoins
    moneycoins +=5






# Section 3 - game loop
window.listen()
for i in range(1000000000):
    
    # TODO - put any repeating actions here

    time.sleep(0.01)
    window.update()