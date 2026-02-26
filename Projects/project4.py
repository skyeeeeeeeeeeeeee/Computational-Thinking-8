import turtle, time, random
from utils import *

# Section 1 - setup
# TODO - set a background using 
set_background("sunset")

# TODO - create at least two variables and set their starting value. ex: cookies = 0
aura_points=0
moneycoins=10



# Section 2 - controls
# Aura points go up one while money goes up ten but you need to keep money over 25 in order for aura point to continue going up and each money sprite is worth 10
# TODO - define an action. ex: def my_control()
def get_aura_points():
    global aura_points, moneycoins
    if moneycoins <25: 
        aura_points -= 5
    elif moneycoins >25:
        aura_points +=1
        x = random.randint(-400,300)
        y = random.randint(-200,300)
        create_sprite("aura points",x,y)
def get_moneycoins():
    global moneycoins
    moneycoins +=10 
    x = random.randint(-400,300)
    y = random.randint(-200,300)
    create_sprite("moneycoins",x,y)

# TODO - choose a key to do the action. ex: window.onkeypress(my_control, "space") 
# TODO - make a second control
#Everytime your press space key you get aura points but in order for your aura points to keep going up you need at least 25 money and you get money by pressing the "m" key
window.onkeypress(get_aura_points, "space")
window.onkeypress(get_moneycoins, "m")








# Section 3 - game loop
window.listen()
for i in range(1000000000):
    
    # TODO - put any repeating actions here

    time.sleep(0.01)
    window.update()