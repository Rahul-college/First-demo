
import turtle
import colorsys

t = turtle.Turtle()
s = turtle.Screen()
s.bgcolor('pink')
t.speed(20)
n=50
h=0
for i in range(200):
    c=colorsys.hsv_to_rgb(h, 1, 0.8)
    h=h+1/n
    t.color(c)
    t.forward(i*2)
    t.left(145)
    turtle.done()