
from tkinter import *
from selenium import webdriver 
import time
from PIL import Image
from pytesseract import image_to_string
import os
from gtts import gTTS
import pygame
myfont = "-family {Segoe UI} -size 13 -weight normal -slant "  \
            "roman -underline 0 -overstrike 0"
labelfont =  "-family {Segoe UI} -size 15 -weight normal -slant "  \
            "roman -underline 0 -overstrike 0"
labelfont1 =  "-family {Segoe UI} -size 17 -weight normal -slant "  \
            "roman -underline 1 -overstrike 0"
inputfont =  "-family {Segoe UI} -size 13 -weight normal -slant "  \
            "roman -underline 0 -overstrike 0"

def readitout(xstext):
	tts = gTTS(xstext)
	tts.save('C:/Users/abhis/Desktop/sdl/pulled/speak.mp3')
	pygame.init()
	pygame.mixer.music.load("C:/Users/abhis/Desktop/sdl/pulled/speak.mp3")
	pygame.mixer.music.play()
	

def hwadjust(gidde):
	gidde.configure(height=1)
	gidde.configure(width=29)
	#gidde.configure(background="#2196f3")
	return gidde

def seperator():
   fseperator = Label(m,text=" ")
   fseperator.pack()
   fseperator.configure(font=myfont)
   fseperator.configure(background="#263238")


def google():
	driver = webdriver.Firefox()
	driver.get("https://www.google.com")
	time.sleep(4)
	searchbar =driver.find_element_by_xpath("//*[@id='lst-ib']")
	submit = driver.find_element_by_xpath("/html/body/div/div[3]/form/div[2]/div[3]/center/input[1]")
	searchbar.send_keys(e.get("1.0",END))
	submit.click()


def shop():
	driver = webdriver.Firefox()
	driver.get("https://www.amazon.in")
	time.sleep(4)
	searchbar =driver.find_element_by_xpath("//*[@id='twotabsearchtextbox']")
	submit = driver.find_element_by_xpath("/html/body/div[1]/header/div/div[1]/div[3]/div/form/div[2]/div/input")
	searchbar.send_keys(e.get("1.0",END))
	submit.click()


def locate():
	driver = webdriver.Firefox()
	driver.get("https://www.google.com/maps/dir///@18.7434171,73.5404431,11z")
	time.sleep(4)
	froml =driver.find_element_by_xpath("/html/body/jsl/div[3]/div[7]/div[3]/div[1]/div[2]/div/div[3]/div[1]/div[1]/div[2]/div/div/input")
	formd =driver.find_element_by_xpath("/html/body/jsl/div[3]/div[7]/div[3]/div[1]/div[2]/div/div[3]/div[1]/div[2]/div[2]/div/div/input")
	submit = driver.find_element_by_xpath("/html/body/jsl/div[3]/div[7]/div[3]/div[1]/div[2]/div/div[3]/div[1]/div[2]/div[2]/button[1]")
	
	froml.send_keys(fromloc.get("1.0",END))
	formd.send_keys(toloc.get("1.0",END))

	submit.click()

def ocr():
	#print("Processing.")
	os.system("adb shell screencap -p /sdcard/snap.png")
	os.system("adb pull /sdcard/snap.png C:/Users/abhis/Desktop/sdl/pulled")
	xtext = image_to_string(Image.open("C:/Users/abhis/Desktop/sdl/pulled/snap.png"),lang='eng')
	nwindow = Toplevel(m)
	showtext = Text(nwindow)
	showtext.insert(END,xtext)
	showtext.pack()
	readitout(xtext)

def compilers():
	print("compilers page !")

def socialpage():
	print("social page!")

m = Tk()
m.configure(background="#263238")
queryy = StringVar()
m.title("LPHI - Let Python Handle It !")
#m.geometry("750x750")
m.resizable(width=False, height=False)

'''
tabarea = tkinter.ttk.Notebook(m)
tab1 = Frame(tabarea)
tab2 = Frame(tabarea)
tabarea.add(tab1,text="Social")
tabarea.add(tab2,text="Compilers")
tabarea.pack()
'''

#button1 = Button(m,text="ok",width=9,command=sett)
maintitle = Label(m,text="LET PYTHON HANDLE IT !")
maintitle.configure(font=labelfont1)
maintitle.configure(background="#263238")
maintitle.configure(foreground="#ffffff")
maintitle.pack()
seperator()

abby = Label(m,text="Type to start searching or shopping !")
abby.pack()
abby.configure(font=labelfont)
abby.configure(background="#263238")
abby.configure(foreground="#ffffff")
seperator()

e = Text(m,height="1",width="8",font=inputfont)
e.pack()
e.focus_set()
#e.configure(foreground="WHITE")
hwadjust(e)
seperator()

button = Button(m,text="Google",width=25,command=google)
button.pack()
button.configure(font=myfont)
button.configure(background="#2196f3")
button.configure(foreground="#ffffff")
seperator()

button1 = Button(m,text="Shop",width=25,command=shop)
button1.pack()
button1.configure(font=myfont)
button1.configure(background="#2196f3")
button1.configure(foreground="#ffffff")
seperator()


maploc = Label(m,text="Set Start Location")
maploc.pack()
maploc.configure(font=inputfont)
maploc.configure(background="#263238")
maploc.configure(foreground="#ffffff")
seperator()

fromloc = Text(m,height="1",width="8",font=inputfont)
fromloc.pack()
fromloc.focus_set()
hwadjust(fromloc)
seperator()

mapdest = Label(m,text="Set End Location")
mapdest.pack()
mapdest.configure(font=inputfont)
mapdest.configure(background="#263238")
mapdest.configure(foreground="#ffffff")
seperator()

toloc = Text(m,height="1",width="8",font=inputfont)
toloc.pack()
toloc.focus_set()
hwadjust(toloc)
seperator()

locatebutton = Button(m,text="Get Directions !",width=25, command=locate)
locatebutton.pack()
locatebutton.configure(font=myfont)
locatebutton.configure(background="#2196f3")
locatebutton.configure(foreground="#ffffff")
seperator()
#
ocrbutton=Button(m,text="Click to read your android screen !",command=ocr)
ocrbutton.pack()
ocrbutton.configure(font=myfont)
ocrbutton.configure(background="#2196f3")
ocrbutton.configure(foreground="#ffffff")
hwadjust(ocrbutton)
#ocrbutton.configure(height=34)
#ocrbutton.configure(width=97)
seperator()

socialpagebtn = Button(m,text="Social Login",command=socialpage)
socialpagebtn.pack(side="left")
hwadjust(socialpagebtn)
socialpagebtn = Button(m,text="Easy Compilers",command=compilers)
socialpagebtn.pack(side="left")
hwadjust(socialpagebtn)


m.mainloop()
