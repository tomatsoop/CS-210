"""
CS 210 Project 1 - Turtle Graphics
Author:[Sabrina Zhang]
Drawing a Duck with Turtle

"""

import turtle
t = turtle.Turtle()

def head():
    t.penup()
    t.forward(100)
    t.pendown()
    t.circle(100)
    t.right(-90)
    t.penup()
    t.forward(120)
    t.right(-90)
    t.forward(15)

def eye():
    t.pendown()
    t.circle(15)
    t.right(180)

def beak():
    t.penup()
    t.forward(115)
    t.pendown()
    t.forward(60)
    t.circle(10,180)
    t.forward(70)

def neck():
    t.penup()
    t.forward(35)
    t.right(-90)
    t.forward(125)
    t.pendown()
    for i in range (3):
        t.forward(100)
        t.right(90)
        t.penup()
        t.pendown()


def body():
    t.right(90)
    t.penup()
    t.forward(100)
    t.right(90)
    t.pendown()
    t.forward(300)
    t.right(-90)
    t.circle(300,45)

def water():
    t.right(45)
    t.penup()
    t.right(90)
    t.forward(100)
    t.pendown()
    t.right(-90)
    for i in range (6):
            t.circle(45,180)
            t.right(-180)

def rest_of_body():
    t.right(180)
    t.penup()
    t.forward(213)
    t.right(-90)
    t.forward(128)
    t.right(-45)
    t.pendown()
    t.right(-90)
    t.circle(-160,105)

def wing():
    t.penup()
    t.right(90)
    t.forward(200)
    t.right(-45)
    t.pendown()
    t.forward(100)
    t.circle(50,180)
    t.forward(100)
    t.circle(50,180)

#Draw the Duck
head()
eye()
beak()
neck()
body()
water()
rest_of_body()
wing()

turtle.done()