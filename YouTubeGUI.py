from tkinter import *
from youtubemodule import Youtube
import requests
import re
import os



yt = Youtube()
YTsearch = Tk()
    
searchQuery = Entry(YTsearch)
searchQuery.pack()

def queried():
    yt.getFirst(searchQuery.get())

def write_video_to_file():
    with open('downloaded.txt', 'w') as f:
        f.write(str(yt.getFirst(searchQuery.get())))
        searcher.create_text(500, 10, text='...Done!')

download = Button(YTsearch, text='Download Video', command=write_video_to_file)
sendquery = Button(YTsearch, text='Search!', command=queried)
searcher = Canvas(YTsearch, width=1000, height=500)

searcher.create_text(300, 50, text='The program opens a tab with the first result of a YouTube query', font=('Times', 11))
searcher.create_text(256, 70, text='Type something in the search box and hit \'Search!\'', font=('Times', 11))
searcher.create_text(150, 20, text='YouTube Searcher', font=('Courier', 20))

youtubelogo = PhotoImage(file='C:\\Users\\leeso\\OneDrive\\Pictures\\source.gif')
searcher.create_image(500, 300, image=youtubelogo)

download.pack()
sendquery.pack()
searcher.pack()
