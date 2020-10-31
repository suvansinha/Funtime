import turtle

wn = turtle.Screen()
wn.bgcolor("black")

t=turtle.Turtle()
t.speed(8)
t.hideturtle()

def drawcircle(x,y):
    t.color("orangered")
    t.penup()
    t.goto(x,y)
    t.begin_fill()
    t.circle(70)
    t.end_fill()
drawcircle(20,0)
drawcircle(-20,0)

def triangle(x,y):
    t.color("yellow")
    t.penup()
    t.goto(x,y)
    for i in range(3):
        t.forward(40)
        t.left(360/3)
    t.end_fill()
triangle(15,80)
triangle(-55,80)
triangle(-20,50)

def mouth():
    t.color("yellow")
    t.up()
    t.goto(-60,40)
    t.down()
    t.begin_fill()
    t.goto(-30,20)
    t.goto(30,20)
    t.goto(60,40)
    t.goto(0,30)
    t.end_fill()
mouth()    
    
def stem():
    t.color("green")
    t.up()
    t.goto(-40,130)
    t.down()
    t.begin_fill()
    t.goto(40,130)
    t.goto(20,150)
    t.goto(10,170)
    t.goto(0,180)
    t.goto(-15,175)
    t.goto(-10,155)
    t.goto(-15,140)
    t.goto(-40,130)
    t.end_fill()
stem()    
    
    