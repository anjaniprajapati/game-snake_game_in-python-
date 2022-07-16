import turtle
import random
import time

delay = 0.1
score = 0
high_score = 0

# snakebodies
bodies=[]
# Creating a window screen
s = turtle.Screen()
s.title("Snake Game")
s.bgcolor("gray") 
# the width and height can be put as user's choice
s.setup(width=600,height=600) 
# wn.tracer(0)


# head of the snake
head = turtle.Turtle()
head.speed(0)
head.shape("circle")
head.color("white")
head.fillcolor("blue")
head.penup()
head.goto(0,0)
head.direction = "stop"                                                                                                       "Stop"


# food in the game
food = turtle.Turtle()
food.speed(0)
# colors = random.choice(['red', 'green', 'black'])
# shapes = random.choice(['square', 'triangle', 'circle'])
food.shape("circle")
food.color("yellow")
food.fillcolor("green")
food.penup()
food.ht()
food.goto(0,200)
food.st()


# score board
sb = turtle.Turtle()
# sb.speed(0)
sb.shape("square")
sb.fillcolor("black")
sb.penup()
sb.ht()
sb.hideturtle()
sb.goto(0,250)  
# sb.write("Score : 0 High Score : 0", align="center",
		# font=("candara", 24, "bold"))

sb.write("Score:0  |  High Score : 0",align="center")

def moveup():
    if head.direction!="down":
        head.direction="up"
def movedown():
    if head.direction!="up":
        head.direction="down"
def moveleft():
    if head.direction!="right":
        head.direction="left"
def moveright():
    if head.direction!="left":
        head.direction="right"
def movestop():
    head.direction="stop"

def move():
    if head.direction=="up":
        y=head.ycor()
        head.sety(y+20)
    if head.direction=="down":
        y=head.ycor()
        head.sety(y-20)
    if head.direction=="left":
        x=head.xcor()
        head.setx(x-20)
    if head.direction=="right":
        x=head.xcor()
        head.setx(x+20)

# Event Handling -key mapping

s.listen()
s.onkey(moveup ,"Up")
s.onkey(movedown ,"Down")
s.onkey(moveleft ,"Left")
s.onkey(moveright ,"Right")
s.onkey(movestop ,"space")

# main loop

while True:
    s.update()

    if head.xcor()>290:
        head.setx(-290)
    if head.xcor()<-290:
        head.setx(290)
    if head.ycor()>290:
        head.sety(-290)
    if head.ycor()<-290:
        head.sety(290)
    # check collision with food
    if head.distance(food)<20:
        x=random.randint(-290,290)
        y=random.randint(-290,290)
        food.goto(x,y)

        # increase the lenght of snake
        body=turtle.Turtle()
        body.speed(0)
        body.penup()
        body.shape("circle")
        body.color("red")
        body.fillcolor("black")
        bodies.append(body)

        # increase the score
        score+=10

        # change the delay
        delay-=0.001

        # update the heighest score
        if score>high_score:
            high_score=score 
        sb.clear()
        # sb.write("Score:{}".format(score))
        sb.write("Score:{} Highest Score:{}".format(score,high_score)) 

    # move the snake bodies
    for index in range(len(bodies)-1,0,-1):
        x=bodies[index-1].xcor()
        y=bodies[index-1].ycor()
        bodies[index].goto(x,y)
    if len(bodies)>0:
        x=head.xcor()
        y=head.ycor()
        bodies[0].goto(x,y)
    move()

    # check collesion with snake boby
    for body in bodies:
        if body.distance(head)<20:
            time.sleep(1)
            head.goto(0,0)
            head.direction="stop"
            # hide bodies
            for body in bodies:
                body.ht()
            bodies.clear

            score=0
            delay=0
            # update Score board
            sb.clear()
            sb.write("Score:{} Highest Score:{}".format(score,high_score)) 
    time.sleep(delay)
# s.mainloop()
