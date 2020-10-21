import turtle
import random


colors  = ["red","green","blue","orange","purple","pink","yellow","dark green","dark red","lime","dark blue","medium violet red",
           "cyan","saddle brown","dark gray","dark orange","medium purple","magenta"]

dark_colors = ["white","red","green","blue","orange","purple","pink","yellow"]


petal_angle = 90

line_width_max = 2.7
line_width_mid = 2
line_width_min = 1
common_bg_color = 'black'



def remote_concentric_circles(circle_turtle,dis_range,radius):
    """ Function to draw Concentric Circles
    Parameters:
    arg1 (turtle class): Turtle Class Refernce
    arg2 (int)         : Distance Range
    arg3 (int)         : Circle Radius 
    Returns:
    None:Returning None
    """
    for i in range(dis_range):
        color = random.choice(dark_colors)
        circle_turtle.color(color)
        circle_turtle.circle(radius*i)
        circle_turtle.up()
        circle_turtle.sety((radius*i)*(-1))
        circle_turtle.down()

    circle_turtle.up()
    circle_turtle.goto(0,0)
    circle_turtle.down()
    
def remote_petal(turtle,radius):
    """ Function to petal
    Parameters:
    arg1 (turtle class): Turtle Class Refernce
    arg2 (int)         : petal radius  
    Returns:
    None:Returning None
    """
    turtle.circle(radius,petal_angle)
    turtle.left(petal_angle)
    turtle.circle(radius,petal_angle)



if __name__ == "__main__":

    turtle.Turtle()
    turtle_screen = turtle.Screen()
    turtle_screen.bgcolor(common_bg_color)
    turtle.speed(0)

    turtle.width(line_width_mid)
    turtle.color(colors[0])
    for i in range(0,154):
        turtle.left(2.5)
        remote_petal(turtle,140)

    turtle.width(line_width_min)
    turtle.color(common_bg_color)
    turtle.fillcolor(colors[12])
    turtle.begin_fill()
    for i in range(0,72):
        turtle.left(5)
        remote_petal(turtle,125)
    turtle.end_fill()

    turtle.width(line_width_mid)
    turtle.color(common_bg_color)
    turtle.fillcolor(colors[6])
    turtle.begin_fill()
    for i in range(0,30):
        turtle.left(6)
        remote_petal(turtle,105)
    turtle.end_fill()

    turtle.width(line_width_min)
    turtle.color(common_bg_color)
    turtle.fillcolor(colors[3])
    turtle.begin_fill()
    for i in range(0,36):
        turtle.left(20)
        remote_petal(turtle,90)
    turtle.end_fill()

    turtle.width(line_width_mid)
    turtle.color(common_bg_color)
    turtle.fillcolor(colors[0])
    turtle.begin_fill()
    for i in range(0,8):
        turtle.left(45)
        remote_petal(turtle,45)
    turtle.end_fill()

    turtle.home()

    turtle.width(line_width_max)
    remote_concentric_circles(turtle,10,3)

    turtle.width(line_width_min)
    turtle.home()
	
    
    turtle.Screen().exitonclick()
