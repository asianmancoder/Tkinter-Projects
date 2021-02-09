from tkinter import *

master = Tk()

calculator = Canvas(master, width=350, height=450, background='white')
equation = Entry(master)

def getEquation():
    calculator.create_text(175, 50, text=f'Result: {eval(equation.get())}')

evaluate = Button(master, text='Evaluate', command=getEquation)

evaluate.pack()
equation.pack()
calculator.pack()
