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
global System

System = platform.system()

document = open("Acsii.tdf","r")
legal = document.read()
document.close()
print(legal)
document = open("legal.tdf","r")
legal = document.read()
document.close()
print(legal)

#---------------------Define internal scripts------------------------------

def WindowsIconPatch(): #this was added for ease of use while testing and writing the software cross-platform.
        if (System == "Windows"):
            myappid = 'org.FailurePoint.Bandlab' 
            ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(myappid)



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

#---------------------Define GUI scripts-------------------------------------  


def MainWindow():
    class Window(QMainWindow):
            def __init__(self):
                super(Window,self).__init__()
                self.browser = QWebEngineView()
            
            

                self.setWindowIcon(QtGui.QIcon('BandLab.ico'))
                self.browser.setUrl(QUrl('https://www.bandlab.com/mix-editor'))
                self.setCentralWidget(self.browser)
                self.showMaximized()

                WindowsIconPatch()
                    
    MyApp = QApplication(sys.argv)
    QApplication.setApplicationName('BandLab Linux Client 2.0')
    window = Window()
    MyApp.exec_()        




def ServerErrorWindow():
    WindowsIconPatch()
    win = Tk()  
    win.title('ERROR')
    win.geometry("800x150")
    win.iconbitmap('BandLab.ico')
    header = Label(win, text = "BandLab appears to be having a problem with it's servers,").place(x = 30,y = 10)
    header = Label(win, text = "The BandLab client is getting no response from: https://bandlab.com but https://google.com is responding fine.").place(x = 30,y = 50)
    header = Label(win, text = "I suggest a large mug of coffee (or tea if your like me) and i good book while you wait... Hopfuly BandLab will have the servers back up soon. ").place(x = 30,y = 70)
    win.mainloop()



def WifiErrorWindow():
    WindowsIconPatch()
    win = Tk()  
    win.title('ERROR')
    win.geometry("420x100")
    win.iconbitmap('BandLab.ico')
    header = Label(win, text = "There appears to be a problem, your offline...").place(x = 30,y = 10)
    header = Label(win, text = "BandLab Client requires internet to load your account and interface.").place(x = 30,y = 50)
    header = Label(win, text = "Plese check your wifi and retry.").place(x = 30,y = 70)
    win.mainloop()




def WelcomeScreen():
    WindowsIconPatch()
    Softwarestate = open("SoftwareStatus.info","w")
    Softwarestate.write("Active = True \n")
    Softwarestate.write("Running on: \n")
    Softwarestate.write(System)
    Softwarestate.close()
    win = Tk()
    win.title('Welcome!')
    win.geometry("1150x300")
    win.iconbitmap('BandLab.ico')
    header = Label(win, text = "Hi There! Welcome to my port of BandLab to Linux!").place(x = 30,y = 10)
    header = Label(win, text = "Before you get started there are a few things i need to say, ").place(x = 30,y = 40)
    header = Label(win, text = "        1. This software is not an offical BandLab program but rather a container to host the webpage version in a more native from.").place(x = 30,y = 70)
    header = Label(win, text = "        2. Due to this i can take no responibility and do nothing about this software not working if the problem is being caused at BandLab.com's end.").place(x = 30,y = 90)
    header = Label(win, text = "        3. This software is capable of visiting external web-page links from withing the main gui, but with that said i do not recomend it.").place(x = 30,y = 110)
    header = Label(win, text = "        4. Please also take note that this software requires you already have a BandLab account, if you do not have one go to: https://www.bandlab.com/sign-up and make an account then come back and finish.").place(x = 30,y = 130)
    header = Label(win, text = "Thats all there is to it! To continue to the app please click the 'OK' button or just close this window.").place(x = 30,y = 160)
    header = Label(win, text = "Good luck and happy Jaming! :)").place(x = 30,y = 180)
    OK = tk.Button(win, text='OK', width=10, command= win.destroy).place(x = 500,y = 230)
    win.mainloop()


        




#-------------------------------Organise and execute above definitions----------------------------------    

try:
    SoftwareStatus = open("SoftwareStatus.info","r")
    SoftwareStatus.close()
except:
    WelcomeScreen()


if Server():
    MainWindow()
   
    
else:

    if InternetCheck():
            print("\n It appears that the BandLab Server is down. Please try again later.")
            ServerErrorWindow()

    else:
        print("Your computer is offline or the internet is down, please connect to a network and try again...")
        WifiErrorWindow()

