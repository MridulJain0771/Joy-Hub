def login():
   pass


from tkinter import *
from PIL import ImageTk,Image

root = Tk()
root.title("JOY HUB")
#root.iconbitmap("icon.jpg")

frame1 = LabelFrame(root, text="frame1")
frame2 = LabelFrame(root, text="frame2")
frame3 = LabelFrame(root, text="Tetris")
frame4 = LabelFrame(root, text="Pong")
frame5 = LabelFrame(root, text="frame5",padx=50,pady=169,bg='grey')


frame1.grid(row=0,column=0)
frame2.grid(row=0,column=1)
frame3.grid(row=1,column=0)
frame4.grid(row=1,column=1)
frame5.grid(row=0,column=2,rowspan=8,sticky=E+W)


image_pong_ = ImageTk.PhotoImage(Image.open("pongf.png"))
image_tetrus_= ImageTk.PhotoImage(Image.open("tetrisf.png"))
image_music_ = ImageTk.PhotoImage(Image.open("musicpagef.png"))
image_vedio_= ImageTk.PhotoImage(Image.open("mirrorf.png"))


login_id = Entry(frame5,width=50,bg="black", fg="white", borderwidth=5)
paswrd = Entry(frame5,width=50,bg="black",fg="red",borderwidth=5)
submit = Button(frame5,text="LogIn",padx=30,pady=5,bg="midnightblue",fg="white",command=login)



image_pong = Label(frame4,image= image_pong_,width=250,height=220,bg='black')
image_tetrus = Label(frame3,image= image_tetrus_,width=250,height=220,bg='black')
image_music = Label(frame2,image= image_music_,width=250,height=220,bg='black')
image_vedio = Label(frame1,image= image_vedio_,width=250,height=220,bg='black')

image_music.grid(row=0,column=0)
image_pong.grid(row=0,column=1)
image_tetrus.grid(row=0,column=2)
image_vedio.grid(row=0,column=4)

user = Label(frame5,text="User Id : ")
user.grid(row=0,column=0)

password = Label(frame5, text = "Password : ")
password.grid(row=2,column=0)

space = Label(frame5, text= "       ",bg='grey')
space.grid(row=1,column=1)

login_id.grid(row=0,column=1)
paswrd.grid(row=2,column=1)


space1 = Label(frame5, text= "       ",bg='grey')
space1.grid(row=3,column=1)

submit.grid(row=4,column=1)

root.mainloop()