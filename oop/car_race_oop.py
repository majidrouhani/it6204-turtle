#Eksemplet er hentet fra: https://trinket.io/python/9339862606
import turtle
from random import randint

# Set up the screen
sc = turtle.Screen()
sc.bgcolor("gray")
sc.setup(width=600, height=600)

ada = turtle.Turtle()
bob = turtle.Turtle()
ivy = turtle.Turtle()
jim = turtle.Turtle()



def draw_finish_line():
  draw = turtle.Turtle()

  draw.speed(0)
  draw.penup()
  draw.goto(-140, 140)

  for step in range(15):
    draw.write(step, align='center')
    draw.right(90)
    for num in range(8):
      draw.penup()
      draw.forward(10)
      draw.pendown()
      draw.forward(10)
    draw.penup()
    draw.backward(160)
    draw.left(90)
    draw.forward(20)

def draw(p_turtle, p_color, p_shape, p_x, p_y, p_range, p_angle):
  p_turtle.color(p_color)
  p_turtle.shape(p_shape)

  p_turtle.penup()
  p_turtle.goto(p_x, p_y)
  p_turtle.pendown()

  for turn in range(p_range):
    p_turtle.right(p_angle)

def celebrate(p_turtle):
  original_color = p_turtle.color()[0]
  p_turtle.penup()
  p_turtle.goto(p_turtle.xcor()-10, p_turtle.ycor())
  p_turtle.pendown()
  p_turtle.color("gold")
  p_turtle.begin_fill()
  p_turtle.circle(20)
  p_turtle.end_fill()
  p_turtle.color(original_color)
  p_turtle.write("WINNER!", font=("Arial", 16, "bold"))

draw_finish_line()
draw(ada, 'red', 'turtle', -160, 100, 10, 36)
draw(bob, 'blue', 'turtle', -160, 70, 72, 5)
draw(ivy, 'green', 'turtle', -160, 40, 60, 6)
draw(jim, 'orange', 'turtle', -160, 10, 30, 12)

min_limit, max_limit = 1, 5
distance = {"ada": 0, "bob": 0, "ivy": 0, "jim": 0}

for i in range(100):
  move = randint(min_limit,max_limit)
  ada.forward(move)
  distance["ada"] += move
  
  move = randint(min_limit,max_limit)
  bob.forward(move)
  distance["bob"] += move

  move = randint(min_limit,max_limit)
  ivy.forward(move)
  distance["ivy"] += move

  move = randint(min_limit,max_limit)
  jim.forward(move)
  distance["jim"] += move

# find the winner turtle
winner = max(distance, key=distance.get)
print(distance)

# find the winner turtle
match winner:
    case "ada":
        celebrate(ada)
    case "bob":
        celebrate(bob)
    case "ivy":
        celebrate(ivy)
    case "jim":
        celebrate(jim)
  
sc.exitonclick()
