import os
import random
import time

#Import the Turtle module
import turtle


##############################################################################

#Created the frame of the game

turtle.fd(0)
#method that controls speed of animation
turtle.speed(0)
#background color
turtle.bgcolor("black")
#Change background color
#turtle.bgpic("moon.gif")
#Change the window title
turtle.title("Space War")
#Hide default turtle
turtle.ht()
#Limits the amount of memory used
turtle.setundobuffer(1)
#speeds up the animation: Frames
turtle.tracer(0)

##############################################################################

#Child of the Turtle Class
class Sprite(turtle.Turtle):

    #Constructor
    def __init__(self, spriteShape, color, startX, startY):
        turtle.Turtle.__init__(self,shape=spriteShape)
        #Speed of animation
        self.speed(0)
        self.penup()
        self.color(color)
        self.fd(0)
        self.goto(startX, startY)
        self.speed = 1

    #default movement method for the sprite class
    def move(self):
        self.fd(self.speed)

        #BOUNDARY DETECTION
        if self.xcor() > 290:
            self.setx(290)
            self.rt(60)

        if self.xcor() < -290:
            self.setx(-290)
            self.rt(60)

        #BOUNDARY DETECTION
        if self.ycor() > 290:
            self.sety(290)
            self.rt(60)

        if self.ycor() < -290:
            self.sety(-290)
            self.rt(60)

    def is_collision(self,other):
        if (self.xcor() >= (other.xcor() - 20)) and (self.xcor() <= (other.xcor() + 20)) and \
           (self.ycor() >= (other.ycor() - 20)) and (self.ycor() <= (other.ycor() + 20)):
                return True
        else:
            return False




###############################################################################

#Child of the Sprite Class

class Player(Sprite):

    #Constructor
    def __init__(self, spriteShape, color, startX, startY):
        Sprite.__init__(self, spriteShape, color, startX, startY)
        self.shapesize(stretch_wid=0.6, stretch_len=1.1, outline= None)
        self.speed = 4
        self.lives = 3

    def turn_left(self):
        #Sprite turns 45 degrees counterClockwise
        self.lt(45)

    def turn_right(self):
        #Sprite turns 45 degrees Clockwise
        self.rt(45)

    def accelerate(self):
        #Move faster
        self.speed += 1

    def decelerate(self):
        #Move slower
        self.speed -= 1


###############################################################################

class Enemy(Sprite):

    #Constructor
    def __init__(self, spriteShape, color, startX, startY):
        Sprite.__init__(self, spriteShape, color, startX, startY)
        self.speed = 6
        self.setheading(random.randint(0, 360))


###############################################################################
class Ally(Sprite):

    #Constructor
    def __init__(self, spriteShape, color, startX, startY):
        Sprite.__init__(self, spriteShape, color, startX, startY)
        self.speed = 8
        self.setheading(random.randint(0, 360))


    def move(self):
        self.fd(self.speed)

        #BOUNDARY DETECTION
        if self.xcor() > 290:
            self.setx(290)
            self.lt(60)

        if self.xcor() < -290:
            self.setx(-290)
            self.lt(60)

        #BOUNDARY DETECTION
        if self.ycor() > 290:
            self.sety(290)
            self.lt(60)

        if self.ycor() < -290:
            self.sety(-290)
            self.lt(60)



###############################################################################

class Missile(Sprite):

    #Constructor
    def __init__(self, spriteShape, color, startX, startY):
        Sprite.__init__(self, spriteShape, color, startX, startY)
        self.shapesize(stretch_wid=0.2, stretch_len=0.4, outline= None)
        self.speed = 20
        self.status = "ready"
        #Wont be able to see atm
        self.goto(-1000, 1000)

    def fire(self):
        if self.status == "ready":
            self.goto(player.xcor(), player.ycor())
            self.setheading(player.heading())
            self.status = "firing"

    def move(self):

        if self.status == "ready":
            self.goto(-1000, 1000)

        if self.status == "firing":
            self.fd(self.speed)

        #BOUNDARY DETECTION
        if (self.xcor() > 290) or (self.xcor() < -290) or \
           (self.ycor() > 290) or (self.ycor() < -290):
            self.goto(-1000, 1000)
            self.status = "ready"








###############################################################################
class Particle(Sprite):

    #Constructor
    def __init__(self, spriteShape, color, startX, startY):
        Sprite.__init__(self, spriteShape, color, startX, startY)
        self.shapesize(stretch_wid=0.1, stretch_len=0.1, outline= None)
        self.goto(-1000, 1000)
        self.frame = 0

    def explode(self,startx, starty):
        self.goto(startx, starty)
        self.setheading(random.randint(0, 360))
        self.frame = 1

    def move(self):
        if self.frame > 0:
            self.fd(10)
            self.frame += 1

        if self.frame > 15:
            self.frame = 0
            self.goto(-1000,1000)



###############################################################################
class Game():
    def __init__(self):
        self.level = 1
        self.score = 0
        self.state = "Playing"
        self.pen = turtle.Turtle()
        self.lives = 3

    def draw_border(self):
        #DRAW BORDER, ANIMATION SPEED
        self.pen.speed(0)
        self.pen.color("white")
        self.pen.pensize(3)
        self.pen.penup()
        self.pen.goto(-300, 300)
        self.pen.pendown()
        for side in range(4):
            self.pen.fd(600)
            self.pen.rt(90)
        self.pen.penup()
        self.pen.ht()
        self.pen.pendown()

    def show_status(self):
        self.pen.undo()
        msg = "Score: %s" %(self.score)
        self.pen.penup()
        self.pen.goto(-300, 310)
        self.pen.write(msg, font=("Arial", 16, "normal"))

################################################################################

#Create game object
game = Game()

#Draw the game border
game.draw_border()

#SHOW THE GAME STATUS
game.show_status()


#Create my Sprite
player = Player("triangle", "white", 0, 0)
#enemy = Enemy("circle", "red", -100, 0)
missile = Missile("triangle", "yellow", 0, 0)
#ally = Ally("square", "blue", 100, 0)

enemies =[]
for i in range(6):
    enemies.append(Enemy("circle", "red", -100, 0))

allies =[]
for i in range(6):
    allies.append(Ally("square", "blue", 100, 0))

particles = []
for i in range(20):
    particles.append(Particle("circle","orange",0,0))


#Keyboard binding
turtle.onkey(player.turn_left, "Left")
turtle.onkey(player.turn_right, "Right")
turtle.onkey(player.accelerate, "Up")
turtle.onkey(player.decelerate, "Down")
turtle.onkey(missile.fire, "space")
turtle.listen()

#Main Game Loop

while True:
    turtle.update()
    time.sleep(0.02)
    player.move()
    #enemy.move()
    missile.move()
    #ally.move()

    for enemy in enemies:
        enemy.move()

        # CHECK FOR COLLISION
        if player.is_collision(enemy):
            x = random.randint(-250, 250)
            y = random.randint(-250, 250)
            enemy.goto(x, y)
            # Decrease score
            game.score -= 100
            game.show_status()

        if missile.is_collision(enemy):
            x = random.randint(-250, 250)
            y = random.randint(-250, 250)
            enemy.goto(x, y)
            missile.status = "ready"

            # increase score
            game.score += 100
            game.show_status()

            #Do Explosion
            for particle in particles:
                particle.explode(missile.xcor(), missile.ycor())

    for ally in allies:
        ally.move()

        if missile.is_collision(ally):
            x = random.randint(-250, 250)
            y = random.randint(-250, 250)
            ally.goto(x, y)
            missile.status = "ready"
            # Decrease score
            game.score -= 100
            game.show_status()

    for particle in particles:
        particle.move()




delay = input("Press Enter >")