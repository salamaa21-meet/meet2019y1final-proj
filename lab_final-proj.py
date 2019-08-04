import turtle
turtle.tracer(1,0)

UP_EDGE = 400
DOWN_EDGE = -500
RIGHT_EDGE = 460
LEFT_EDGE = -460
#Window size

#Box is the reqtangle where we see the riddles
box=turtle.clone()
box.color('red', 'lightgreen')
box.begin_fill()
box.hideturtle()
box.penup()
box.goto(460,400)
box.pendown()
box.goto(460,200)
box.goto(-460,200)
box.goto(-460,400)
box.goto(460,400)
box.end_fill()
#The question's box is ready


