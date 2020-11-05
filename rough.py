def lengthdown():
    ml = mixer.music.get_pos() // 1000
    print(ml)
    mixer.music.set_pos(ml - 5.0)
    tl = mixer.music.get_pos() // 1000
    print(tl)
    CurrentSongLength = mixer.music.get_pos() // 1000

    progressbarmusicstartLabel.configure(text='{}'.format(str(datetime.timedelta(seconds=CurrentSongLength))))
    progressbarmusic['value'] = CurrentSongLength
def lengthup():
    ml = mixer.music.get_pos() // 1000
    print(ml)
    mixer.music.set_pos(ml + 5.0)
    tl = mixer.music.get_pos() // 1000
    print(tl)
    CurrentSongLength = mixer.music.get_pos() // 1000

    progressbarmusicstartLabel.configure(text='{}'.format(str(datetime.timedelta(seconds=CurrentSongLength))))
    progressbarmusic['value'] = CurrentSongLength

def unmute():
    global currentvol
    mp.unmutebutton.grid_remove()
    mp.mutebutton.grid()
    mixer.music.set_volume(currentvol)
    audiostatuslabel.configure(text='Playing...')
def mute():
    global currentvol
    mp.mutebutton.grid_remove()
    mp.unmutebutton.grid()
    currentvol = mixer.music.get_volume()
    mixer.music.set_volume(0)
    audiostatuslabel.configure(text='Muted...')

def resume():
    mp.ResumeButton.grid_remove()
    mp.PauseButton.grid()
    mixer.music.unpause()
    audiostatuslabel.configure(text='Playing...')
def stop():
    mixer.music.stop()
    audiostatuslabel.configure(text='Stopped...')


def volumeup():
    vol = mixer.music.get_volume()
    if(vol*100<=75):
        mixer.music.set_volume(vol+0.1)
    else:
        mixer.music.set_volume(vol + 0.01)
    ProgressbarVolumeLabel.configure(text='{}%'.format(int(mixer.music.get_volume()*100)))
    ProgressbarVolume['value'] = mixer.music.get_volume()*100

def volumedown():
    vol = mixer.music.get_volume()
    if (vol * 100 >= 25):
        mixer.music.set_volume(vol - 0.1)
    else:
        mixer.music.set_volume(vol - 0.01)
    ProgressbarVolumeLabel.configure(text='{}%'.format(int(mixer.music.get_volume() * 100)))
    ProgressbarVolume['value'] = mixer.music.get_volume() * 100
def pause():
    mixer.music.pause()
    mp.PauseButton.grid_remove()
    mp.ResumeButton.grid()
    audiostatuslabel.configure(text='Paused...')
def playmusic():
    ad = audiotrack.get()
    mixer.music.load(ad)
    progressbarLabel.grid()
    progressbarmusicLabel.grid()
    mp.mutebutton.grid()
    mixer.music.set_volume(0.6)
    mixer.music.play()
    audiostatuslabel.configure(text='Playing...')

    Song = MP3(ad)
    totalsonglength = int(Song.info.length)
    progressbarmusic['maximum'] = totalsonglength
    progressbarmusicendLabel.configure(text='{}'.format(str(datetime.timedelta(seconds=totalsonglength))))
    def progressbarmusictick():



        CurrentSongLength = mixer.music.get_pos() // 1000
        if(CurrentSongLength!=-1):
            progressbarmusic['value'] = CurrentSongLength
            progressbarmusicstartLabel.configure(text='{}'.format(str(datetime.timedelta(seconds=CurrentSongLength))))
            progressbarmusic.after(2, progressbarmusictick)
        else:
            CurrentSongLength = 0
            progressbarmusic['value'] = CurrentSongLength
            progressbarmusicstartLabel.configure(text='{}'.format(str(datetime.timedelta(seconds=CurrentSongLength))))
            progressbarmusic.after(2, progressbarmusictick)
    progressbarmusictick()

def musicurl():
    try:
        dd = filedialog.askopenfilename(initialdir='C:/Users/mridu/Downloads',
                                        title='Select Audio File',
                                        filetype=(('MP3','*.mp3'),('WAV','*.wav')))
    except:
        dd = filedialog.askopenfilename(title='Select Audio File',
                                        filetype=(('MP3','*.mp3'),('WAV','*.wav')))
    audiotrack.set(dd)


def createlabel():
    global audiostatuslabel,ProgressbarVolumeLabel,ProgressbarVolume,progressbarLabel,progressbarmusicendLabel,progressbarmusic,progressbarmusicstartLabel,progressbarmusicLabel
    global implay,imsearch,imstop,impause,immute,imunmute,imvolup,imvoldow
    #image button
    implay = PhotoImage(file='playf.png')
    imsearch = PhotoImage(file='search.png')
    imstop = PhotoImage(file='stopf.png')
    impause = PhotoImage(file='pausef.png')
    immute = PhotoImage(file='mutef.png')
    imunmute = PhotoImage(file='unmutef.png')
    imvolup = PhotoImage(file='volumeupf.png')
    imvoldow = PhotoImage(file='volumedownf.png')


    #size of button
    implay = implay.subsample(1,1)
    #lable
    TrackLabel = Label(mp,text='Select Audio Track : ', background='CadetBlue1',font=('arial',15,'italic bold'))
    TrackLabel.grid(row=0,column=0,padx=20,pady=20)

    audiostatuslabel = Label(mp,text='', background='red2',font=('arial',15,'italic bold'),width=20)
    audiostatuslabel.grid(row=2,column=1)
    #entry box
    Tracklableentry = Entry(mp,font=('arial',16,'italic bold'),width=35,textvariable=audiotrack)
    Tracklableentry.grid(row=0,column=1,padx=20,pady=20)
    #button
    #searchbutton
    BrowseButton= Button(mp,text='Search',bg='cyan2',font=('arial',13,'italic bold'),width=100,bd=0,
                         activebackground='purple4',command=musicurl,image=imsearch,compound=RIGHT)
    BrowseButton.grid(row=0,column=2,padx=20,pady=20)
    #playbutton
    mp.PlayButton= Button(mp,text='Play  ',  bg='orange', font=('arial', 13, 'italic bold'), width=100, bd=0,
                          activebackground='purple4',command=playmusic,image =implay,compound=RIGHT)
    mp.PlayButton.grid(row=1, column=0, padx=20, pady=20)
    #pausebutton
    mp.PauseButton = Button(mp, text='Pause  ', bg='cyan2', font=('arial', 13, 'italic bold'), width=100, bd=0,
                        activebackground='purple4',command=pause,image =impause,compound=RIGHT)
    mp.PauseButton.grid(row=1, column=1, padx=20, pady=20)
    # resumebutton
    mp.ResumeButton = Button(mp, text='Resume  ', bg='orange', font=('arial', 13, 'italic bold'), width=100, bd=5,
                         activebackground='purple4', command=resume,image =implay,compound=RIGHT)
    mp.ResumeButton.grid(row=1, column=1, padx=20, pady=20)
    mp.ResumeButton.grid_remove()
    #mutebutton
    mp.mutebutton=Button(mp,text='Mute  ',width=80,bg='orange',activebackground='purple',bd=5,command=mute,image =immute,compound=RIGHT)
    mp.mutebutton.grid(row=3,column=3)
    mp.mutebutton.grid_remove()
    # unmutebutton
    mp.unmutebutton = Button(mp, text='Unmute  ', width=80, bg='orange', activebackground='purple', bd=5,command=unmute,image =imunmute,compound=RIGHT)
    mp.unmutebutton.grid(row=3, column=3)
    mp.unmutebutton.grid_remove()
    #volumeup
    VolumeupButton = Button(mp, text='Volume Up ', bg='orange', font=('arial', 13, 'italic bold'), width=140, bd=5,
                        activebackground='purple4',command=volumeup,image =imvolup,compound=RIGHT)
    VolumeupButton.grid(row=1, column=2, padx=20, pady=20)
    # stopbutton
    StopButton = Button(mp, text='Stop ', bg='orange', font=('arial', 13, 'italic bold'), width=100, bd=0,
                        activebackground='purple4',command=stop,image =imstop,compound=RIGHT)
    StopButton.grid(row=2, column=0, padx=20, pady=20)
    # volumedown
    VolumeDownButton = Button(mp, text='Volume Down ', bg='orange', font=('arial', 13, 'italic bold'), width=140, bd=5,
                            activebackground='purple4',command=volumedown,image =imvoldow,compound=RIGHT)
    VolumeDownButton.grid(row=2, column=2, padx=20, pady=20)
#progressbar volume
    progressbarLabel = Label(mp,text='',bg='red')
    progressbarLabel.grid(row=0,column=3,rowspan=3,padx=20,pady=20)
    progressbarLabel.grid_remove()
    ProgressbarVolume = Progressbar(progressbarLabel,orient=VERTICAL,mode='determinate',
                                    value=60,length=190)
    ProgressbarVolume.grid(row=0,column=0,ipadx=5)

    ProgressbarVolumeLabel = Label(progressbarLabel,text='60%',bg='lightgray',width=3)
    ProgressbarVolumeLabel.grid(row=0,column=0)
#Progresbarmusic
    progressbarmusicLabel =Label(mp,text='',bg='red')
    progressbarmusicLabel.grid(row=4,column=0,columnspan=3,padx=20,pady=20)
    progressbarmusicLabel.grid_remove()

    progressbarmusicstartLabel = Label(progressbarmusicLabel, text='0.00.0', bg='red',width=10)
    progressbarmusicstartLabel.grid(row=0, column=0)

    progressbarmusic = Progressbar(progressbarmusicLabel,orient=HORIZONTAL,mode='determinate',value=0)
    progressbarmusic.grid(row=0,column=1,ipadx=370)


    progressbarmusicendLabel = Label(progressbarmusicLabel, text='0.00.0', bg='red')
    progressbarmusicendLabel.grid(row=0, column=2)
#musiclengthincresing
    musiclengthinc = Button(mp, text='>>>', bg='cyan2', font=('arial', 13, 'italic bold'), width=20, bd=5,
                              activebackground='purple4', command=lengthup)
    musiclengthinc.grid(row=3, column=1, padx=20, pady=20)
#musiclengthdecresing
    musiclengthdec = Button(mp, text='<<<', bg='cyan2', font=('arial', 13, 'italic bold'), width=20, bd=5,
                              activebackground='purple4', command=lengthdown)
    musiclengthdec.grid(row=3, column=0, padx=20, pady=20)
#
from tkinter import *
#from PIL import Image,ImageTk
from tkinter import filedialog
from pygame import mixer
from tkinter.ttk import Progressbar
import datetime
from mutagen.mp3 import MP3
mp = Tk()
mp.geometry('1100x500+100+100')
mp.title('Music Player')
mp.iconbitmap('music.ico')
mp.resizable(False,False)
mp.configure(bg='black')
#
c=0
audiotrack = StringVar()
currentvol = 0
totalsonglength =0
ss = ' Joy Hub '
count = 0

#slider

text = ''
SliderLabel= Label(mp,text=ss,bg='gray50',font=('arial', 40, 'italic bold'))
SliderLabel.grid(row=6,column=1,padx=20,pady=20)
def IntroLabel():
    global count,text
    if(count>=len(ss)):
        count = -1
        text = ''
        SliderLabel.configure(text=text)
    else:
        text = text+ss[count]
        SliderLabel.configure(text=text)
    count += 1
    SliderLabel.after(200,IntroLabel)
IntroLabel()
mixer.init()
createlabel()
mp.mainloop()
