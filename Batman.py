import turtle
import math

myPen = turtle.Turtle()
myPen.speed(500)
    
window = turtle.Screen()
window.bgcolor("black")
myPen.color("yellow")

zoom=20

myPen.left(90)
myPen.penup()
myPen.goto(-7*zoom,0)
myPen.pendown()

for i in range(-7*zoom,-3*zoom,1):
  x=i/zoom
  absx=math.fabs(x)
  y=1.5*math.sqrt((-math.fabs(absx-1))*math.fabs(3-absx)/((absx-1)*(3-absx)))*(1+math.fabs(absx-3)/(absx-3))*math.sqrt(1-(x/7)**2)+(4.5+0.75*(math.fabs(x-0.5)+math.fabs(x+0.5))-2.75*(math.fabs(x-0.75)+math.fabs(x+0.75)))*(1+math.fabs(1-absx)/(1-absx))
  myPen.goto(i,y*zoom)

for j in range(-3*zoom,-1*zoom-1,1):
  x=j/zoom
  absx=math.fabs(x)
  y=(2.71052+1.5-0.5*absx-1.35526*math.sqrt(4-(absx-1)**2))*math.sqrt(math.fabs(absx-1)/(absx-1))
  myPen.goto(j,y*zoom)
  
myPen.goto(-1*zoom,3*zoom)
myPen.goto(int(-0.5*zoom),int(2.2*zoom))
myPen.goto(int(0.5*zoom),int(2.2*zoom))
myPen.goto(1*zoom,3*zoom)

for k in range(1*zoom+1,3*zoom+1,1):
  x=k/zoom
  absx=math.fabs(x)
  y=(2.71052+1.5-0.5*absx-1.35526*math.sqrt(4-(absx-1)**2))*math.sqrt(math.fabs(absx-1)/(absx-1))
  myPen.goto(k,y*zoom)

for l in range(3*zoom+1,7*zoom+1,1):
  x=l/zoom
  absx=math.fabs(x)
  y = 1.5*math.sqrt((-math.fabs(absx-1))*math.fabs(3-absx)/((absx-1)*(3-absx)))*(1+math.fabs(absx-3)/(absx-3))*math.sqrt(1-(x/7)**2)+(4.5+0.75*(math.fabs(x-0.5)+math.fabs(x+0.5))-2.75*(math.fabs(x-0.75)+math.fabs(x+0.75)))*(1+math.fabs(1-absx)/(1-absx))
  myPen.goto(l,y*zoom)

for p in range(7*zoom,4*zoom,-1):
  x=p/zoom
  absx=math.fabs(x)
  y=(-3)*math.sqrt(1-(x/7)**2) * math.sqrt(math.fabs(absx-4)/(absx-4))
  myPen.goto(p,y*zoom)

for q in range(4*zoom,-4*zoom,-1):
  x=q/zoom
  absx=math.fabs(x)
  y=math.fabs(x/2)-0.0913722*x**2-3+math.sqrt(1-(math.fabs(absx-2)-1)**2)
  myPen.goto(q,y*zoom)

for r in range(-4*zoom-1,-7*zoom-1,-1):
  x=r/zoom
  absx=math.fabs(x)
  y =(-3)*math.sqrt(1-(x/7)**2) * math.sqrt(math.fabs(absx-4)/(absx-4))
  myPen.goto(r,y*zoom)
  
myPen.penup()
myPen.goto(300,300)
