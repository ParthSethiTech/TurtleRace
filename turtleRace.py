

from turtle import *

from random import randint

import operator



speed(0)

penup()

goto(-40,160)

color('green')

style = {'Arial',24,'bold'}



#Header

write("Welcome to Turtle race!", align='center', font=style)



goto(-140,140)

hideturtle()

color('grey')

allTurtles = {'Parth':0,'Mukesh':0,'Joe':0,'Salman':0}



for step in range(16):

    write(" ",align='center')

    right(90)

    forward(10)

    for p in range(10):

        pendown()

        forward(10)

        penup()

        forward(5)

    backward(160)

    left(90)

    forward(20)



#Turtle 1

Parth = Turtle()

#Parth.color('Orange')

Parth.color('#FFA500')

Parth.shape('turtle')

Parth.penup()

Parth.goto(-235,100)

Parth.write("Parth")

Parth.penup()

Parth.goto(-160,100)

Parth.pendown()

Parth.right(360)



#Turtle 2

Mukesh = Turtle()

Mukesh.color('blue')

Mukesh.shape('turtle')

Mukesh.penup()

Mukesh.goto(-235,70)

Mukesh.write("Mukesh")

Mukesh.penup()

Mukesh.goto(-160,70)

Mukesh.pendown()

Mukesh.right(360)



#Turtle 3

Joe = Turtle()

Joe.color('red')

Joe.shape('turtle')

Joe.penup()

Joe.goto(-235,40)

Joe.write("Joe")

Joe.penup()

Joe.goto(-160,40)

Joe.pendown()

Joe.right(360)



#Turtle 4

Salman = Turtle()

Salman.color('purple')

Salman.shape('turtle')

Salman.penup()

Salman.goto(-235,10)

Salman.write("Salman")

Salman.penup()

Salman.goto(-160,10)

Salman.pendown()

Salman.right(360)





for turn in range(105):

    Parth.forward(randint(1,5,))

    Mukesh.forward(randint(1,5,))

    Joe.forward(randint(1,5,))

    Salman.forward(randint(1,5,))



allTurtles['Parth'] = int(Parth.xcor())

allTurtles['Mukesh'] = int(Mukesh.xcor())

allTurtles['Joe'] = int(Joe.xcor())

allTurtles['Salman'] = int(Salman.xcor())





print(allTurtles)



allTurtles_s = sorted(allTurtles.items(), key=operator.itemgetter(1),reverse=True)



color('Orange')

goto(-40,-50)

write("The winner is : " + allTurtles_s[0][0], align='center', font=style)