import turtle             
my_window = turtle.Screen()        
my_window.bgcolor("black")
my_pen = turtle.Turtle()      
 
turtle.speed(0)
 
colors = ["red", "purple", "blue", "green", "yellow", "orange"]
 
for i in range(300):
    my_pen.color(colors[i%6])
    my_pen.width(i/100 + 1)
    my_pen.forward(i)           
    my_pen.left(59)
    
turtle.done()
turtle.hideturtle()