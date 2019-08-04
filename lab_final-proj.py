import turtle
import time
turtle.tracer(1,0)

UP_EDGE = 400
DOWN_EDGE = -500
RIGHT_EDGE = 460
LEFT_EDGE = -460

screen=turtle.clone()
turtle.register_shape("bgpic.gif")
screen.shape("bgpic.gif")
screen.shapesize(1000,900)

#Window size and screen

#Box is the reqtangle where we see the riddles
box=turtle.clone()
box.color('red', 'lightgreen')
box.begin_fill()
box.hideturtle()
box.penup()
box.goto(460,500)
box.pendown()
box.goto(460,300)
box.goto(-460,300)
box.goto(-460,500)
box.goto(460,500)
box.end_fill()
#The question's box is ready

turtle.register_shape('tree1.gif')
turtle.register_shape('tree2.gif')
