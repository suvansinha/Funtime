from turtle import *

speed(0)
bgcolor("black")
pensize(3)

for x in range(5):
     for colours in ["red","magenta","blue","cyan","green","yellow","white"]:
         color(colours)
         left(12)
         for i in range(4):
             forward(200)
             left(90)
             
         