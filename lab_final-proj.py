import turtle
import time
turtle.tracer(1,0)


screen = turtle.Screen()
screen.setup(1000,1500)

UP_EDGE = 400
DOWN_EDGE = -500
RIGHT_EDGE = 460
LEFT_EDGE = -460

screen=turtle.clone()
turtle.register_shape("bgpic.gif")
screen.shape("bgpic.gif")
screen.shapesize(1000,900)
#Window size and screen

q="1.what are the plants and trees release into the air?"
a="a.air   b.oxygin  c.music  d.zack's fart"
q1="what colour is the trash can you put the boxes in?"
a1="a.Orange b.Blue c.Green d.Black"
q2="scientists say that till 2050 there will be more plastic than fish in the oceans"
a2="True      False"
q3="in the worldwide, how many single-use plastic bags are used per year?"
a3="a.300,000  b.6 Billions  c.500 Billions  d.2 Trillions"


ques=[q,q1,q2,q3]
ans=[a,a1,a2,a3]
nq=ques[0]

"""
def new_ques():
    global nq
    index_ques = ques.index(nq)
    nq = ques[index_ques+1]
    new_ques()
"""


tx=turtle.clone()
tx.penup()
tx.goto(-450,450)
tx.write(q, font=("Arial", 30, " normal"))
tx.hideturtle()

ans=turtle.clone()
ans.penup()
ans.goto(-350,350)
ans.write(a, font=("Arial", 30, " normal"))
ans.hideturtle()

"""

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
"""

#here we are registering the tree pics
turtle.register_shape('tree1.gif')
turtle.register_shape('tree2.gif')
turtle.register_shape('tree3.gif')
turtle.register_shape('tree4.gif')

turtle.register_shape('tree5.gif')
turtle.register_shape('tree6.gif')
turtle.register_shape('tree7.gif')
turtle.register_shape('tree8.gif')

#here we put them in a variables
tree1='tree1.gif'
tree2='tree2.gif'
tree3='tree3.gif'
tree4='tree4.gif'
tree5='tree5.gif'
tree6='tree6.gif'
tree7='tree7.gif'
tree8='tree8.gif'

#plants is the list where there are the trees variables
plants=[tree1,tree2,tree3,tree4,tree5,tree6,tree7,tree8]

#plant is the variable where we put the other varibales of the trees so we be able to change them later
plant=plants[0]

#index_plants = plants.index(plant)
#x=plants[index_plants+1]
#to be continued


#here we put the first shape
tree=turtle.clone()
tree.shape(plant)
tree.pensize(10)
tree.penup()
tree.goto(0,50)

#when we answer the questions correctly, we will print "correct!" and change the pic
def correct():
    print("Correct!")
    global plant
    index_plants = plants.index(plant)
    plant=plants[index_plants+1]
    tree.shape(plant)

def incorrect():
    print("incorrect")
    global plant
    index_plants = plants.index(plant)
    plant=plants[index_plants-1]
    tree.shape(plant)    
#The questions
x = 0
score = x

# Question One 
print("What are the plants and trees release into the air?")
answer_1 = input("a)air\nb)oxygen\nc)music\nd)zak's fart \n:")
if answer_1.lower() == "b" or answer_1.lower() == "oxygen":
    correct()
    x = x + 1   
else:
    incorrect()

# Question Two
print("What color is the trash can you put the boxes in")
answer_2 = input("a) orange\nb)blue\nc)green\nd)black\n:")
if answer_2.lower() == "a" or answer_2.lower() == "orange":
    correct()
    x = x + 1
else:
    incorrect()

# Question Three
print("True or False... scientists say that till 2050 there will be more plastic than fish in the ocean?")
answer_3 = input(":")
if answer_3.lower() == "true" or answer_3.lower() == "t":
    correct()
    x = x + 1
else:
    incorrect()
     
# Question Four
print("In the worldwide, how many single-use plastic bags are used per year?")
answer_4 = input("a)300,000\nb)6 billions\nc)500 billions\nd)2 trillions\n:")
if answer_4.lower() == "c" or answer_4 == "500 billions":
    correct()
    x = x + 1
else:
    incorrect()

# Question Five 
print("True or False... 60,000 marine creaturs are dying from plactic entanglement every year")
answer_5 = input(":")
if answer_5.lower() == "false" or answer_5.lower() == "f":
    correct()
    x = x + 1
else:
    incorrect()


    # Question six
print("How many people die everyday as result of drinking unclean water")
answer_1 = input("a)1000\nb)300\nc)5000\nd)2670\n:")
if answer_1.lower() == "c" or answer_1.lower() == "5000":
    correct()
    x = x + 1   
else:
    incorrect()

# Question seven
print("What is the world's largest producer of carbon dioxide?")
answer_2 = input("a)USA\nb)China\nc)france\nd)italy\n:")
if answer_2.lower() == "b" or answer_2.lower() == "China":
    correct()
    x = x + 1
else:
    print("Incorrect, it's China")

# Question eight
print("True or False... acidification of the ocean is the worst type of pollution?")
answer_3 = input(":")
if answer_3.lower() == "true" or answer_3.lower() == "t":
    correct()
    x = x + 1
else:
    incorrect()

# Question nine
print("How many kilograms of garbage a single person use i the USA?")
answer_4 = input("a)0.5\nb)1\nc)3\nd)2\n:")
if answer_4.lower() == "d" or answer_4 == "2":
    correct()
    x = x + 1
else:
    incorrect()
          

# Question ten 
print("The pollution in China doesn't change the weather in the USA?")
answer_5 = input(":")
if answer_5.lower() == "false" or answer_5.lower() == "f":
    correct()
    x = x + 1
else:
    incorrect()


#Total Score
score = float(x / 10) * 100
print(x,"out of 10, that is",score, "%")







