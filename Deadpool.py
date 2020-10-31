import turtle as t, time

t.color('red')
t.penup()
t.goto(0, -200)
t.pendown()

t.begin_fill()  
t.circle(200) 
t.end_fill()

def black_circle():
    t.begin_fill()
    t.color('black')
    t.circle(160, -160)
    t.end_fill()

t.goto(0, -160)
t.circle(160, -10)
black_circle()

t.color('red')

t.goto(25, 160)
t.rt(20)
black_circle()

def eye(a):
    t.begin_fill()
    t.goto(a * 40, 0)
    t.color('white')
    t.pendown()
    t.goto(a * 140, 45)
    t.goto(a * 120, 10)
    t.goto(a * 40, 0)
    t.end_fill()
    t.penup()
eye(1)      
eye(-1)     

t.hideturtle()
time.sleep(8)