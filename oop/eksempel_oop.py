import turtle
wn = turtle.Screen()
wn.bgcolor("lightgreen")


rektangel = turtle.Turtle()
rektangel.pensize(5)

trekant = turtle.Turtle()
trekant.color("hotpink")

rektangel.forward(80)
rektangel.left(120)
rektangel.forward(80)
rektangel.left(120)
rektangel.forward(80)
rektangel.left(120)

rektangel.right(180)
rektangel.forward(80)

trekant.forward(50)
trekant.left(90)
trekant.forward(50)
trekant.left(90)
trekant.forward(50)
trekant.left(90)
trekant.forward(50)
trekant.left(90)

wn.exitonclick()
