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
q2="scientists say that till 2050 there will be more plastic -"
pq="than fish in the ocean." 
a2="True            False"
q3="in the worldwide, how many single-use plastic bags are -"
pq1="used per year?"  
a3="a.300,000  b.6 Billions  c.500 Billions  d.2 Trillions"
q4="60,000 marine creatures are dying from plastic entanglement every year"
a4="True      False"
q5="How many people die every day as result of drinking unclean water?"
a5="a.1000     b.300         c.5000         d.2670"
q6="What is the world's largest producer of carbon dioxide"
a6="a.USA      b.China       c.France       d.Italy"
q7="acidifiscation of the ocean is the worst type of pollution"
a7="True     False"
q8="How many killograms of garbage a single person does in the USA"
a8="a.0.5     b.1            c.3            d.2"
q9="The pollution is China doesn't change the weather in the USA"
a9="True     False"

#here we put the questions and the answers in variables (we are going to do the same thing we did in the trees)

ques=[q,q1,q2,q3,q4,q5,q6,q7,q8,a9]
partq=[pq,pq1]
ans=[a,a1,a2,a3,a4,a5,a6,a7,a8,a9]
#we put them in a list
nq=ques[0]
npq=partq[0]
na=ans[0]
#we are putting one variable and its going to be changed as its position in the list


tx=turtle.clone()
tx.penup()
tx.goto(-480,450)
tx.write(nq, font=("Arial", 30, " normal"))
tx.hideturtle()
#here we print the questions

an=turtle.clone()
an.penup()
an.goto(-480,350)
an.write(na, font=("Arial", 30, " normal"))
an.hideturtle()

prq=turtle.clone()
prq.penup()
prq.goto(-480,400)
prq.write(npq, font=("Arial", 30, " normal"))
prq.hideturtle()





def new_ques():
    tx.clear()
    global nq
    index_ques = ques.index(nq)
    nq = ques[index_ques+1]
    

    tx.penup()
    tx.goto(-480,450)
    tx.write(nq, font=("Arial", 30, " normal"))
    tx.hideturtle()
#a function to change the questions every time

def new_ques():
    tx.clear()
    global nq
    index_partq = partq.index(npq)
    npq = partq[index_partq+1]
    

    prq.penup()
    prq.goto(-480,000)
    prq.write(npq, font=("Arial", 30, " normal"))
    prq.hideturtle()

def new_answer():
    an.clear()
    global na
    index_ans = ans.index(na)
    na = ans[index_ans + 1]

    an.penup()
    an.goto(-480,350)
    an.write(na, font=("Arial", 30, " normal"))
    an.hideturtle()

    


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
    new_ques()
    new_answer()

def incorrect():
    print("incorrect")
    global plant
    index_plants = plants.index(plant)
    plant=plants[index_plants-1]
    
    tree.shape(plant)
    new_ques()
    new_answer()
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
    print("Incorrect")
    

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







