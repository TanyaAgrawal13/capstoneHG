import turtle
turtle.color("black","pink")
turtle.begin_fill()
for i in range(5):
    turtle.forward(50)
    turtle.right(144)
turtle.end_fill()

turtle.penup()
turtle.goto(100,0)
turtle.pendown()
turtle.begin_fill()
for i in range(5):
    turtle.forward(70)
    turtle.right(144)
turtle.end_fill()    
turtle.penup()
turtle.goto(220,0)
turtle.pendown()
turtle.begin_fill()
for i in range(5):
    turtle.forward(90)
    turtle.right(144)
turtle.end_fill()