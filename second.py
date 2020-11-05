
def login():
    def close_window():
        l.destroy()
    global image_pong_, image_music_,image_vedio_,image_tetrus_
    l=Tk()
    l.title("Login")
    l.geometry('1000x500+100+100')
    frame1 = LabelFrame(l, text="frame1")
    frame2 = LabelFrame(l, text="frame2")
    frame3 = LabelFrame(l, text="Tetris")
    frame4 = LabelFrame(l, text="Pong")
    frame5 = LabelFrame(l, text="frame5", padx=50, pady=169, bg='grey')

    frame1.grid(row=0, column=0)
    frame2.grid(row=0, column=1)
    frame3.grid(row=1, column=0)
    frame4.grid(row=1, column=1)
    frame5.grid(row=0, column=2, rowspan=8, sticky=E + W)

    login_id = Entry(frame5, width=50, bg="black", fg="white", borderwidth=5)
    paswrd = Entry(frame5, width=50, bg="black", fg="red", borderwidth=5)
    submit = Button(frame5, text="LogIn", padx=30, pady=5, bg="midnightblue", fg="white", command = close_window)

    image_pong_ = ImageTk.PhotoImage(Image.open("pongf.png"),master=l)
    image_tetrus_ = ImageTk.PhotoImage(Image.open("tetrisf.png"),master=l)
    image_music_ = ImageTk.PhotoImage(Image.open("musicpagef.png"),master=l)
    image_vedio_ = ImageTk.PhotoImage(Image.open("mirrorf.png"),master=l)

    image_pong = Label(frame4, image=image_pong_, width=250, height=220, bg='black')
    image_tetrus = Label(frame3, image=image_tetrus_, width=250, height=220, bg='black')
    image_music = Label(frame2, image=image_music_, width=250, height=220, bg='black')
    image_vedio = Label(frame1, image=image_vedio_, width=250, height=220, bg='black')

    image_music.grid(row=0, column=0)
    image_pong.grid(row=0, column=1)
    image_tetrus.grid(row=0, column=2)
    image_vedio.grid(row=0, column=4)

    user = Label(frame5, text="User Id : ")
    user.grid(row=0, column=0)

    password = Label(frame5, text="Password : ")
    password.grid(row=2, column=0)

    space = Label(frame5, text="       ", bg='grey')
    space.grid(row=1, column=1)

    login_id.grid(row=0, column=1)
    paswrd.grid(row=2, column=1)

    space1 = Label(frame5, text="       ", bg='grey')
    space1.grid(row=3, column=1)

    submit.grid(row=4, column=1)

    l.mainloop()
def musicplayer():
    import main
def pong():
    import pong_game_extra
def tetris():
    import  tetris
def mirror():
    import R
#from tkinter import filedialog
from tkinter import *
import tkinter as tk
import time
from PIL import ImageTk,Image
#from main import *
class slider:
    def __init__(self,sp):
        self.sp=sp
        #self.sp.title("slider")
        #self.sp.geometry("1350x700+0+0")
        #==#
        self.image1=ImageTk.PhotoImage(file="musicpagef.png")
        self.image2 = ImageTk.PhotoImage(file="tetrisf.png")
        self.image3 = ImageTk.PhotoImage(file="pongf.png")
        self.image4 = ImageTk.PhotoImage(file="mirrorf.png")

        #la
        Frame_slider=Frame(self.sp)
        Frame_slider.grid(row=1, column=0,columnspan=3,rowspan=6)
        self.lbl1=Label(Frame_slider,image=self.image1,bg='black', width = 1090,height=200,relief=tk.RIDGE, bd=5)#,bg='black', width = 1000,height=200,relief=tk.RIDGE, bd=5
        self.lbl1.grid(row=1, column=0,columnspan=3,rowspan=6)
        self.lbl2 = Label(Frame_slider, image=self.image2,bg='black', width = 1090,height=200,relief=tk.RIDGE, bd=5)
        self.lbl2.grid(row=1, column=0,columnspan=3,rowspan=6)
        self.lbl3 = Label(Frame_slider, image=self.image3, bg='black', width=1090, height=200, relief=tk.RIDGE, bd=5)
        self.lbl3.grid(row=1, column=0, columnspan=3, rowspan=6)
        self.lbl4 = Label(Frame_slider, image=self.image4, bg='black', width=1090, height=200, relief=tk.RIDGE, bd=5)
        self.lbl4.grid(row=1, column=0, columnspan=3, rowspan=6)
        self.x=180
        self.slider_func()

    def slider_func(self):

        self.x-=1
        if self.x==0:
            self.x=180
            time.sleep(3)
            #swap
            self.new_im=self.image1
            self.image1=self.image2
            self.image2 = self.image3
            self.image3 = self.image4
            self.image4=self.new_im

            self.lbl1.config(image=self.image1)
            self.lbl2.config(image=self.image2)
            self.lbl3.config(image=self.image3)
            self.lbl4.config(image=self.image4)
        #self.lbl2.place(x=self.x,y=0)
        self.lbl2.after(40,self.slider_func)


sp = Tk()
sp.geometry('1100x625+0+0')
sp.resizable(False,False)
implay = PhotoImage(file='playf.png')
immusicplayer = PhotoImage(file='musicpagef.png')
immirror = PhotoImage(file='mirrorf.png')
imtetris = PhotoImage(file='tetrisf.png')
impong = PhotoImage(file='pongf.png')
imlogo = PhotoImage(file='logof.png')
sp.configure(bg='dimgray')
    #image button

logo = Label(sp, text='JOY HUB',bg='medium spring green', font=('arial', 13, 'italic bold'),relief=tk.RIDGE, width=36, bd=10,borderwidth = 5)
logo.grid(row=0, column=0)
user = Label(sp, text='@PygammersProduction',bg='medium spring green', font=('arial', 13, 'italic bold'), width=35,relief=tk.RIDGE, bd=5)
user.grid(row=0, column=1)
madeby =Button(sp, text='Login',bg='red', font=('arial', 13, 'italic bold'), width=35,relief=tk.RIDGE, bd=5,command=login)
madeby.grid(row=0, column=2)


#slider2 = Label(sp,image=immirror, font=('arial', 13, 'italic bold'),bg='black', width = 1000,height=200,relief=tk.RIDGE, bd=5)
#slider2.grid(row=1, column=0,columnspan=3,rowspan=6)
obj=slider(sp)

Game1 = Button(sp, image = immusicplayer,text='Music Player', width=350,bg='black', activebackground='purple', bd=5,command=musicplayer)
Game1.grid(row=7, column=0)
Game2 = Button(sp, image = imtetris, width=350,bg='black',  activebackground='purple', bd=5,command=tetris)
Game2.grid(row=7, column=2)
logoima = Label(sp,  image = imlogo, width=350,height=250,bg='black',   activebackground='purple', bd=5)
logoima.grid(row=7, column=1,rowspan=8,pady=50)
Game3 = Button(sp, image = impong, width=350,bg='black',   activebackground='purple', bd=5,command=pong)
Game3.grid(row=9, column=0)
Game4 = Button(sp, image = immirror,  width=350,bg='black', activebackground='purple', bd=5,command=mirror)
Game4.grid(row=9, column=2)


# get a series of gif images you have in the working folder
# or use full path, or set directory to where the images are
image_files = [
'mirrorf.png',
'pongf.png',
'tetrisf.png',
'musicpagef.png'
]

sp.mainloop()