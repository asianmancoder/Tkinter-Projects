from tkinter import *

master = Tk()

calculator = Canvas(master, width=350, height=450, background='white')
equation = Entry(master)

def getEquation():
    result = Label(master, text=eval(equation.get()))
    result.pack()

evaluate = Button(master, text='Evaluate', command=getEquation)

evaluate.pack()
equation.pack()
calculator.pack()
