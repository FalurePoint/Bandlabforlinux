import sys
import ctypes
import os 
import platform

import urllib.request
from PyQt5.QtWidgets import *
from PyQt5.QtWebEngineWidgets import *
from PyQt5.QtCore import *
from PyQt5 import QtGui
import tkinter as tk
from tkinter import *


global OldUrl
global CurrentUrl
global Regestered
Regestered = False

version = open("version.info","r")
version = version.read()
OST = platform.system()
OSTF = open("OStype.info","w")
OSTF.write(OST)
OSTF.close()
OSV = platform.release()
OSVF = open("OSversion.info","w")
OSVF.write(OSV)
OSVF.close()
OSP = platform.platform()
OSPF = open("OSplatform.info","w")
OSPF.write(OSP)
OSPF.close()
raw = open("root file directory.fdir","r")
root = raw.read()

System = open("OStype.info","r")
System = System.read()
document = open("legal.txt","r")
legal = document.read()
document.close()
print(legal)

def WindowsIconPatch():
        myappid = 'org.AlphaLinux.Bandlab' 
        ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(myappid)



try:
    Softwarestate = open("Active.info","r")
except:
    Softwarestate = open("Active.info","w")
    Softwarestate.write("Software is curently active!")
    Softwarestate.close()
    if (System == "Windows"):
        WindowsIconPatch()
    win = Tk()
    win.title('Welcome!')
    win.geometry("1150x300")
    win.iconbitmap('BandLab.ico')
    header = Label(win, text = "Hi There! Welcome to my port of BandLab to Linux!").place(x = 30,y = 10)
    header = Label(win, text = "Before you get started there are a few things i need to say, ").place(x = 30,y = 40)
    header = Label(win, text = "        1. This software is not an offical BandLab program but rather a container to host the webpage version in a more native from.").place(x = 30,y = 70)
    header = Label(win, text = "        2. Due to this i can take no responibility and do nothing about this software not working if the problem is being caused at BandLab.com's end.").place(x = 30,y = 90)
    header = Label(win, text = "        3. This software is capable of visiting external web-page links from withing the main gui, but with that said i do not recomend it.").place(x = 30,y = 110)
    header = Label(win, text = "        4. Please also take note that this software requires you alreddy have a BandLab account, if you do not have one go to: https://www.bandlab.com/sign-up and make an account then come back and finish.").place(x = 30,y = 130)
    header = Label(win, text = "Thats all there is to it! To continue to the app please click the 'OK' button and the software will automaticly regester you, or if for whatever reason you don't want to, just close this window.").place(x = 30,y = 160)
    header = Label(win, text = "Good luck and happy Jaming! :)").place(x = 30,y = 180)
    OK = tk.Button(win, text='OK', width=10, command= win.destroy).place(x = 500,y = 230)
    win.mainloop()

    

def Server(host='https://www.bandlab.com'):
    try:
        urllib.request.urlopen(host)
        return True
    except:
        return False

def InternetCheck(host='https://google.com'):
    try:
        urllib.request.urlopen(host)
        return True
    except:
        return False
        
    



if Server():
    class Window(QMainWindow):
        def __init__(self):
            super(Window,self).__init__()
            self.browser = QWebEngineView()
            
            

            self.setWindowIcon(QtGui.QIcon('BandLab.ico'))
            self.browser.setUrl(QUrl('https://www.bandlab.com/mix-editor'))
            OldUrl = (self.browser.url().toString())
            UrL = (self.browser.url().toString())
            print(OldUrl)
            self.setCentralWidget(self.browser)
            self.showMaximized()
                    
    
    if (System == "Windows"):
        WindowsIconPatch()


    
    MyApp = QApplication(sys.argv)
    QApplication.setApplicationName('BandLab Linux Client 1.0')
    window = Window()
    MyApp.exec_()
   
    
else:

    if InternetCheck():
            print("It appears that the BandLab Server is down. Please try again later.")
            if (System == "Windows"):
                WindowsIconPatch()
            win = Tk()  
            win.title('ERROR')
            win.geometry("700x150")
            win.iconbitmap('BandLab.ico')
            header = Label(win, text = "BandLab appears to be having a problem with it's servers,").place(x = 30,y = 10)
            header = Label(win, text = "The BandLab client is getting no response from: https://bandlab.com but https://google.com is responding fine.").place(x = 30,y = 50)
            header = Label(win, text = "The best thing you can do at this point is sit back and wait... Hopfuly BandLab will have the servers back up soon. ").place(x = 30,y = 70)
            win.mainloop()
    else:
        print("Your computer is offline, client will not load.")
        if (System == "Windows"):
            WindowsIconPatch()
        win = Tk()  
        win.title('ERROR')
        win.geometry("420x100")
        win.iconbitmap('BandLab.ico')
        header = Label(win, text = "There appears to be a problem, your offline...").place(x = 30,y = 10)
        header = Label(win, text = "BandLab Client requires internet to load your account and interface.").place(x = 30,y = 50)
        header = Label(win, text = "Plese check your wifi and retry.").place(x = 30,y = 70)
        win.mainloop()


