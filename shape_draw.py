import turtle
#vriable
size = 100
sides = 6
angle = 360/sides
clr = "green"

#define function
def draw_polygone():
    turtle.color(clr)
    for i in range(sides):
        turtle.forward(size)
        turtle.left(angle)
    turtle.end_fill()
    turtle.hideturtle()

draw_polygone()

t = turtle.Turtle()
secondRowColors = ["", "green"]
for i in range(1, 2):
  t.penup()
  t.pencolor(secondRowColors[i])
  t.goto(i*55, 2)
  t.pendown()
  t.circle(70)

t = turtle.Turtle()

s = 70

for _ in range(4):
    t.forward(s) # Forward turtle by s units
    t.left(90)  # Turn turtle by 90 degree