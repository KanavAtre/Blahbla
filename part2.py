from tkinter import *
from tkinter import messagebox
from tkinter import font
import tkinter 
from PIL import ImageTk, Image
from tkinter import CENTER
from playsound import playsound
import tkvideo
from time import sleep
import pygame
import mysql.connector
import pyautogui


window=Tk()

def data(event):
    if event==1:
        data=E1.get()
        print(str(data))
        messagebox.showinfo("info", "We need to call the pygame function here")
        #pick str(data) and insert into the sql database

def play():
    pygame.mixer.init()
    pygame.mixer.music.load("/Users/thispc/Downloads/Space-Invader-main/background.wav")
    pygame.mixer.music.play(loops=5)
    

def action(value):
    if value=="back":
        messagebox.showinfo("name", "someone please fix the main menu button")
    if value == "PLAY!":
        img.place(x=100000,y=100000)
        Button_quit.place(x=100000,y=100000)
        Button_sql.place(x=100000,y=100000)
        Button_play.place(x=100000,y=100000)
        L1.place(x=100000,y=100000)
        global my_label
        my_label = Label(window)
        my_label.place(x=0,y=0)
        player = tkvideo.tkvideo("Screen Recording 2021-07-07 at 10.45.16 AM.mov", my_label, loop = 5, size = (1500,1000))
        player.play()
        play()
        fontstyle7=("Garamond", 20, "bold") 
        mainmenu=Button(window, text="<-- Main menu", font= fontstyle7, command=lambda:action("back"))
        mainmenu.place(x=100, y=50)
        fontstyle6=("Garamond", 35, "bold") 

        L2=Label(window, text="Enter your username", bg="light blue", font=fontstyle6)
        L2.place(x=600, y=180)

        global E1
        E1=Entry(window, font=fontstyle7)
        E1.place(x=640, y=400)


        Button_continue=Button(window, height=3, width=17, font= fontstyle7, text="Click to continue-->", command=lambda:data(1))
        Button_continue.place(x=650, y=520)


        print("call the pygame function here")

    elif value == "QUIT":
        messagebox.showinfo("warning","We quit the window here")
        print("We quit the window here")

    elif value == "LEADERBOARD!":
        messagebox.showinfo("info2","sql database here")
        print("Show the mysql database here")

                    

image = Image.open('Img_space_bg.png')
# The (450, 350) is (height, width)
image = image.resize((1500, 1000), Image.ANTIALIAS)
my_img = ImageTk.PhotoImage(image)
img = Label(window,image = my_img)
img.place(x=0,y=0)

image_2=Image.open("ScreenshotStarfield.png")
img_resize=image_2.resize((10,20),Image.ANTIALIAS)
img_bg=ImageTk.PhotoImage(img_resize)

fontstyle=("Garamond", 35, "bold")

L1=Label(window, text="SPACE INVADERS", font=fontstyle, bg="light blue")

L1.place(x=580, y=200)

fontstyle2=("Garamond", 29)
Button_play=Button(window, text='PLAY!', width=6, height=2, font=fontstyle2, bg="light blue", command=lambda:action(mytext2))
Button_play.place(x=1000, y=500)
mytext2=Button_play.cget('text')

fontstyle3=("Garamond", 29)
Button_sql=Button(window, text='LEADERBOARD!',height=2, width=17, font=fontstyle2, bg="light blue", command=lambda:action(mytext3))
Button_sql.place(x=600, y=500)
mytext3=Button_sql.cget('text')

fontstyle4=("Garamond", 29)
Button_quit=Button(window, text='QUIT', font=fontstyle2, height=2, width=8,bg="light blue", command=lambda:action(mytext4))
Button_quit.place(x=300, y=500)
mytext4=Button_quit.cget('text')

window.geometry("1500x1000")

window.mainloop()