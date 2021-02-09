from tkinter import *
from youtubemodule import Youtube
import requests
import re




yt = Youtube()
YTsearch = Tk()
    
searchQuery = Entry(YTsearch)
searchQuery.pack()

def queried():
    yt.getFirst(searchQuery.get())
    
sendquery = Button(YTsearch, text='Search!', command=queried)
canvas = Canvas(YTsearch, width=1000, height=500)

canvas.create_text(300, 50, text='The program opens a tab with the first result of a YouTube query', font=('Times', 11))
canvas.create_text(256, 70, text='Type something in the search box and hit \'Search!\'', font=('Times', 11))
canvas.create_text(150, 20, text='YouTube Searcher', font=('Courier', 20))

youtubelogo = PhotoImage(file='C:\\Users\\leeso\\OneDrive\\Pictures\\source.gif')
canvas.create_image(500, 300, image=youtubelogo)

sendquery.pack()
canvas.pack()
