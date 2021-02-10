from tkinter import *
from turtle import *

t = Pen()

master = Tk()
drawAShape = Canvas(master, width=500, height=300)
shapeQuery = Label(master, text='What kind of shape do you want me to draw?')
shapeInfo = Label(master, text='I can draw circles, squares, rectangles and triangles! Tell me what kind of shape you want me to draw in the box below, then click the button above!')

whatShape = Entry(master)

def drawShape():
    if whatShape.get().lower() == "square":
        t.forward(50)
        t.right(90)
        t.forward(50)
        t.right(90)
        t.forward(50)
        t.right(90)
        t.forward(50)
    elif whatShape.get().lower() == "rectangle":
        t.forward(100)
        t.right(90)
        t.forward(50)
        t.right(90)
        t.forward(100)
        t.right(90)
        t.forward(50)
    elif whatShape.get().lower() == "circle":
        r = 50
        t.circle(r)
    elif whatShape.get().lower() == "cool circle":
        r = 10
        n = 10
        
        for i in range(n + 1, 1, -1):
            t.circle(r * i)
    elif whatShape.get().lower() == "triangle":
        t.forward(50)
        t.left(130)
        t.forward(50)
        t.left(115)
        t.forward(50)
    elif whatShape.get().lower() == "spiral circle":
        r = 10
        
        for i in range(100): 
            t.circle(r + i, 45)
    elif whatShape.get().lower() == "cocentric circle":
        r = 10
        
        for i in range(10): 
            t.circle(r * i) 
            t.up() 
            t.sety((r * i)*(-1)) 
            t.down()
    
draw = Button(master, text='Draw', command=drawShape)

draw.pack()
shapeQuery.pack()
shapeInfo.pack()
whatShape.pack()
drawAShape.pack()
