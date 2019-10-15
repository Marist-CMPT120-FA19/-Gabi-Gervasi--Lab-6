#Gabi Gervasi
#Gabrielle.Gervasi1@marist.edu
#Lab 6
#Traffic Light Using Functions

from graphics import *

win= GraphWin("Traffic_light" , 500, 500)

#rectangle for body of the stop light
def draw_light_body(x, y, length, width):
    body=Rectangle (Point(x,y), Point(length, width))
    body.setOutline("black")
    body.setFill("white")
    body.draw(win)

#Circles for stoplight
def draw_lamp(color, a, b, radius):
    lamp = Circle(Point(a,b), radius)
    lamp.setOutline("black")
    lamp.setFill(color)
    lamp.setWidth(3)
    lamp.draw(win)

#Colors for stop light 
def draw_traffic_light(x, y):
    draw_light_body(x,y,90, 153)
    draw_lamp("red", 60,35,20)
    draw_lamp("yellow", 60,82,20)
    draw_lamp("green", 60,128, 20)

draw_traffic_light(30,10)
