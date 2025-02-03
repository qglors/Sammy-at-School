# Initialize Pygame
import pgzrun

# Set window dimensions
WIDTH, HEIGHT = 1000, 650

# variables/objects
points = 0

########################################################################### home/main menu

background = Actor("bedroom")

play_button = Actor("play_button")
play_button.x = 735
play_button.y = 365

########################################################################### bathroom objects

faucet = Actor("faucet")
faucet.x = 470
faucet.y = 210

brush = Actor("brush")
brush.x = 200
brush.y = 325

closebrush = Actor("closebrush")
closebrush.x = 10000

########################################################################### bathroom timers

sink_animation = False  # Sink animation state
sink_timer = 0
brush_animation = False  # Brush movement animation state
brush_x = 200  # Initial x-position for the closebrush
closebrush_speed = 10  # Speed of the horizontal movement
brush_move = "NO"
sink_move = "NO"
paste_appear = "NO"
brush_timer = 0
brush_timer_go = "NO"

########################################################################### kitchen objects

plastic_bag = Actor("plasticbag")
plastic_bag.x = 693
plastic_bag.y = 452

container = Actor("container")
container.x = 556
container.y = 89

bread1 = Actor("bread")
bread1.x = 103
bread1.y = 143

bread = Actor("bread")
bread.x = 103
bread.y = 143

mayo = Actor("mayo")
mayo.x = 880
mayo.y = 452

ham = Actor("ham")
ham.x = 135
ham.y = 392

lettuce = Actor("lettuce")
lettuce.x = 828
lettuce.y = 125

sandwichbag = Actor("plasticbag")
sandwichbag.x = 323
sandwichbag.y = 117

########################################################################### kitchen timers

bread_go = "NO"
bread_timer = 0
bread_timer_go = "NO"

########################################################################### street objects

buspass = Actor("busid")
buspass.x = 562
buspass.y = 468

keys = Actor("keys")
keys.x = 400
keys.y = 468

########################################################################### classroom objects

ipad = Actor("ipad")
ipad.x = 330
ipad.y = 465

notebook = Actor("notebook")
notebook.x = 729
notebook.y = 465

########################################################################### cafeteria objects

recycling = Actor("recycling")
recycling.x = 299
recycling.y = 212

garbage = Actor("garbage")
garbage.x = 503
garbage.y = 211

compost = Actor("compost")
compost.x = 702
compost.y = 218

banana = Actor("banana")
banana.x = 496
banana.y = 460

milk = Actor("milk")
milk.x = 280
milk.y = 460

########################################################################### cafeteria timers

pick_bin = "NO"
pick_item = "YES"
item = ""
hold_banana = "NO"
hold_milk = "NO"
hold_sandwich = "NO"

rain_timer = 0

mx = 0
my = 0

scene = 0

def draw():
    global scene, paste_appear, pick_bin, pick_item, item, rain_timer
    if scene == 0:
        background.draw()
        play_button.draw()

    elif scene == 1:
        screen.clear()
        faucet.draw()
        background.draw()
        if paste_appear == "YES":
            brush.draw()
        closebrush.draw()

    elif scene == 2:
        screen.clear()
        background.draw()
        bread1.draw()
        ham.draw()
        lettuce.draw()
        mayo.draw()
        bread.draw()
        container.draw()
        sandwichbag.draw()

    elif scene == 3:
        screen.clear()
        background.draw()
        keys.draw()
        buspass.draw()

    elif scene == 4:
        screen.clear()
        background.draw()
        notebook.draw()
        ipad.draw()

    elif scene == 5:
        screen.clear()
        background.draw()
        recycling.draw()
        garbage.draw()
        compost.draw()
        banana.draw()
        milk.draw()
        plastic_bag.draw()

    elif scene == 6:
        screen.clear()
        background.draw()



def update():
    global scene, sink_move, brush_move, brush_timer, brush_timer_go, bread_timer, bread_timer_go, bread_go, pick_bin, pick_item, item, rain_timer, mx, my
    if scene == 1:
        if sink_move == "YES":
            bathroom_animation()
        if brush_move == "YES":
            brush_movement_animation()
        if brush_timer_go == "YES":
            brush_timer += 0.02
    if scene == 2:
        if bread_timer_go == "YES":
            bread_timer += 1
        if bread_timer > 20:
            bread_go = "YES"

    if scene == 5:
        if hold_banana == "YES":
            banana.x = mx
            banana.y = my
        elif hold_milk == "YES":
            milk.x = mx
            milk.y = my
        elif hold_sandwich == "YES":
            plastic_bag.x = mx
            plastic_bag.y = my

        if milk.x == 10000 and plastic_bag.x == 10000 and banana.x == 10000:
            background.image = "rain1"
            scene = 6

    if scene == 6:
        rain_timer += 0.2

        if rain_timer > 15:
            rain_timer = 0

        if rain_timer <= 5:
            background.image = "rain1"
        elif rain_timer <= 10:
            background.image = "rain2"
        elif rain_timer <= 15:
            background.image = "rain3"
    print(pick_item)



def on_mouse_move(pos, rel, buttons):
    global mx, my
    mx = pos[0]
    my = pos[1]

def on_mouse_down(pos, button):
    global scene, sink_move, brush_move, paste_appear, points, brush_timer_go, bread_go, bread_timer_go, pick_bin, pick_item, item, rain_timer,hold_banana, hold_milk, hold_sandwich
    if scene == 0:
        if play_button.collidepoint(pos):
            scene = 1
            background.image = "sink3"

    elif scene == 1:
        if faucet.collidepoint(pos):
            print(sink_move)
            if sink_move == "YES":
                sink_move = "NO"
                background.image = "sink3"
            elif sink_move == "NO":
                paste_appear = "YES"
                sink_move = "YES"

        if brush.collidepoint(pos):
            if brush_move == "YES":
                closebrush.x = 10000
                brush_move = "NO"
            elif brush_move == "NO":
                closebrush.x = 600
                brush_move = "YES"
                if paste_appear == "YES":
                    points += 1
                brush_timer_go = "YES"
        if background.collidepoint(pos):
            if brush_timer >= 10:
                background.image = "kitchen"
                scene = 2

    elif scene == 2:
        if bread1.collidepoint(pos):
            bread1.x = 500
            bread1.y = 324
            bread_timer_go = "YES"
        if bread_go == "YES":
            if bread.collidepoint(pos):
                bread.x = 500
                bread.y = 324
        if ham.collidepoint(pos):
            ham.x = 508
            ham.y = 320
        if lettuce.collidepoint(pos):
            lettuce.x = 500
            lettuce.y = 324
        if mayo.collidepoint(pos):
            mayo.x = 494
            mayo.y = 319
        if sandwichbag.collidepoint(pos):
            points += 1
            background.image = "street"
            scene = 3
        elif container.collidepoint(pos):
            background.image = "street"
            scene = 3
    elif scene == 3:
        if keys.collidepoint(pos):
            points += 1
            background.image = "classroom"
            scene = 4
        if buspass.collidepoint(pos):
            background.image = "classroom"
            scene = 4
    elif scene == 4:
        if ipad.collidepoint(pos):
            background.image = "cafeteria"
            scene = 5
        elif notebook.collidepoint(pos):
            points += 1
            background.image = "cafeteria"
            scene = 5

    elif scene == 5:
        if pick_item == "YES":
            if banana.collidepoint(pos):
                hold_banana = "YES"
                pick_item = "NO"
                pick_bin = "YES"
                item = "BANANA"
            if milk.collidepoint(pos):
                hold_milk = "YES"
                milk.x = pos[0]
                milk.y = pos[1]
                pick_item = "NO"
                pick_bin = "YES"
                item = "MILK"
            if plastic_bag.collidepoint(pos):
                hold_sandwich = "YES"
                plastic_bag.x = pos[0]
                plastic_bag.y = pos[1]
                pick_item = "NO"
                pick_bin = "YES"
                item = "BAG"

        if pick_bin == "YES":
            if recycling.collidepoint(pos):
                if item == "BANANA":
                    hold_banana = "NO"
                    points +=1
                    banana.x = 10000
                    banana.y = 10000

                elif item == "MILK":
                    hold_milk = "NO"
                    milk.x = 10000
                    milk.y = 10000

                elif item == "BAG":
                    hold_sandwich = "NO"
                    points +=1
                    plastic_bag.x = 10000
                    plastic_bag.y = 10000

            elif garbage.collidepoint(pos):
                if item == "BANANA":
                    hold_banana = "NO"
                    points +=1
                    banana.x = 10000
                    banana.y = 10000

                elif item == "MILK":
                    hold_milk = "NO"
                    points +=1
                    milk.x = 10000
                    milk.y = 10000

                elif item == "BAG":
                    hold_sandwich = "NO"
                    plastic_bag.x = 10000
                    plastic_bag.y = 10000
            elif compost.collidepoint(pos):
                if item == "BANANA":
                    hold_banana = "NO"
                    banana.x = 10000
                    banana.y = 10000

                elif item == "MILK":
                    hold_milk = "NO"
                    points +=1
                    milk.x = 10000
                    milk.y = 10000

                elif item == "BAG":
                    hold_sandwich = "NO"
                    points +=1
                    plastic_bag.x = 10000
                    plastic_bag.y = 10000

            pick_bin = "NO"
            pick_item = "YES"





########################################################################### bathroom functions

# Function to handle sink animation
def bathroom_animation():
    global sink_timer, background
    sink_timer += 0.5
    if sink_timer > 10:
        sink_timer = 0
    if sink_timer <= 5:
        background.image = "sink1"
    elif sink_timer <= 10:
        background.image = "sink2"
    print(sink_timer)

# Function for closebrush horizontal movement animation
def brush_movement_animation():

    # Move the brush horizontally
    # Reverse direction when reaching bounds
    if closebrush.x >= 520:
        closebrush.x-=30
        print(closebrush.x)

    elif closebrush.x < 520:
        closebrush.x+=30
        print(closebrush.x)



