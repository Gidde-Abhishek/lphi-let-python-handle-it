
from tkinter import *
from selenium import webdriver 
import time
from PIL import Image
from pytesseract import image_to_string
import os
from gtts import gTTS
import pygame
from bs4 import BeautifulSoup
import requests
import csv
import webbrowser



os.system("cls")
print("LPHI - Let Python Handle It !")
print("A Project by :")
print("Abhishek C. Gidde")
print("Janvi V. Saddi")
print("Harshal R. Patil")
myfont = "-family {Segoe UI} -size 13 -weight normal -slant "  \
            "roman -underline 0 -overstrike 0"
labelfont =  "-family {Segoe UI} -size 15 -weight normal -slant "  \
            "roman -underline 0 -overstrike 0"
labelfont1 =  "-family {Segoe UI} -size 17 -weight normal -slant "  \
            "roman -underline 0 -overstrike 0"
inputfont =  "-family {Segoe UI} -size 13 -weight normal -slant "  \
            "roman -underline 0 -overstrike 0"

def grabnews():
	csv_file = open('E-Newspaper.csv','w')
	csv_writer = csv.writer(csv_file)
	news_source = requests.get("https://timesofindia.indiatimes.com/india").text
	soup = BeautifulSoup(news_source,"html5lib")
	csv_writer.writerow(['H E A D L I N E S','L I N K'])
	for headlines in soup.find_all("span",class_="w_tle"):
	    headline = headlines.a.text
	    newslink = headlines.a['href']
	    csv_writer.writerow([headline,newslink])

	csv_file.close()
	os.system('"C:/Program Files (x86)/Microsoft Office/root/Office16/excel.exe" E-newspaper.csv')



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


def google(e):
	driver = webdriver.Firefox()
	driver.get("https://www.google.com")
	time.sleep(4)
	searchbar =driver.find_element_by_xpath("//*[@id='lst-ib']")
	submit = driver.find_element_by_xpath("/html/body/div/div[3]/form/div[2]/div[3]/center/input[1]")
	searchbar.send_keys(e.get("1.0",END))
	submit.click()


def shop(e):
	driver = webdriver.Firefox()
	driver.get("https://www.amazon.in")
	time.sleep(4)
	searchbar =driver.find_element_by_xpath("//*[@id='twotabsearchtextbox']")
	submit = driver.find_element_by_xpath("/html/body/div[1]/header/div/div[1]/div[3]/div/form/div[2]/div/input")
	searchbar.send_keys(e.get("1.0",END))
	submit.click()


def locate(fromloc,mapdest):
	driver = webdriver.Firefox()
	driver.get("https://www.google.com/maps/dir///@18.7434171,73.5404431,11z")
	time.sleep(4)
	froml =driver.find_element_by_xpath("/html/body/jsl/div[3]/div[7]/div[3]/div[1]/div[2]/div/div[3]/div[1]/div[1]/div[2]/div/div/input")
	formd =driver.find_element_by_xpath("/html/body/jsl/div[3]/div[7]/div[3]/div[1]/div[2]/div/div[3]/div[1]/div[2]/div[2]/div/div/input")
	submit = driver.find_element_by_xpath("/html/body/jsl/div[3]/div[7]/div[3]/div[1]/div[2]/div/div[3]/div[1]/div[2]/div[2]/button[1]")
	
	froml.send_keys(fromloc.get("1.0",END))
	formd.send_keys(mapdest.get("1.0",END))

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
	os.system("cls")
	print("LPHI - Let Python Handle It !")
	print("A Project by :")
	print("Abhishek C. Gidde")
	print("Janvi V. Saddi")
	print("Harshal R. Patil")


def twitter(username,password,post):
	driver = webdriver.Firefox()
	driver.get("https://twitter.com/login")
	time.sleep(4)
	searchbar =driver.find_element_by_xpath("/html/body/div[1]/div[2]/div/div/div[1]/form/fieldset/div[1]/input")
	lassword =driver.find_element_by_xpath("/html/body/div[1]/div[2]/div/div/div[1]/form/fieldset/div[2]/input")
	submit = driver.find_element_by_xpath("/html/body/div[1]/div[2]/div/div/div[1]/form/div[2]/button")
	searchbar.send_keys(username.get("1.0",END))
	lassword.send_keys(password.get())
	submit.click()
	time.sleep(4)
	postbox = driver.find_element_by_xpath("//*[@id='tweet-box-home-timeline']")
	#postbox = driver.find_element_by_xpath("")
	time.sleep(1)
	postbtn = driver.find_element_by_xpath("/html/body/div[2]/div[2]/div/div[2]/div[2]/div/form/div[3]/div[2]/button")
	#initpostbox.click()
	postbox.send_keys(post.get("1.0",END))
	#wheretopost.click()
	postbtn.click()


def facebook(username,password):
	driver = webdriver.Firefox()
	driver.get("https://www.facebook.com/login/device-based/regular/login")
	time.sleep(4)
	searchbar =driver.find_element_by_xpath("//*[@id='email']")
	lassword =driver.find_element_by_xpath("//*[@id='pass']")
	submit = driver.find_element_by_xpath("//*[@id='loginbutton']")
	searchbar.send_keys(username.get("1.0",END))
	lassword.send_keys(password.get())
	submit.click()
	'''time.sleep(4)
	initpostbox = driver.find_element_by_xpath("/html/body/div[1]/div[3]/div[1]/div/div[2]/div[2]/div[1]/div[2]/div/div[3]/div/div/div[2]/div/div/div/div/div[2]/div/div[1]/div/div[1]/div[2]")
	postbox = driver.find_element_by_xpath("/html/body/div[1]/div[3]/div[1]/div/div[2]/div[2]/div[1]/div[2]/div/div[3]/div/div/div[2]/div[1]/div/div/div/div[2]/div/div[1]/div/div[1]/div[2]/div/div/div/div/div/div/div[2]/div/div/div/div")
	wheretopost = driver.find_element_by_xpath("/html/body/div[1]/div[3]/div[1]/div/div[2]/div[2]/div[1]/div[2]/div/div[3]/div/div/div[2]/div[1]/div/div/div/div[2]/div/div[2]/div[3]/div[1]/div/ol/li[1]/div[1]/ol/li/div/div[1]/div")
	postbtn = driver.find_element_by_xpath("/html/body/div[1]/div[3]/div[1]/div/div[2]/div[2]/div[1]/div[2]/div/div[3]/div/div/div[2]/div[1]/div/div/div/div[2]/div/div[2]/div[3]/div[2]/div/div/span/button")
	initpostbox.click()
	postbox.send_keys(post)
	wheretopost.click()
	postbtn.click()'''

def twitterpageinit(page):
	twpage = Toplevel(page)
	usernamelabel = Label(twpage,text="Username / Mobile :")
	usernamelabel.pack()
	usernamelabel.configure(font=labelfont)
	usernamelabel.configure(background="#263238")
	usernamelabel.configure(foreground="#ffffff")
	username = Text(twpage,height="1",width="8",font=inputfont)
	username.pack()
	username.focus_set()
	#e.configure(foreground="WHITE")
	hwadjust(username)
	passwordlabel = Label(twpage,text="Password :")
	passwordlabel.pack()
	passwordlabel.configure(font=labelfont)
	passwordlabel.configure(background="#263238")
	passwordlabel.configure(foreground="#ffffff")
	hwadjust(passwordlabel)
	password = Entry(twpage,font=inputfont,show="*")
	password.pack()
	password.focus_set()

	#e.configure(foreground="WHITE")
	#hwadjust(password)
	postlabel = Label(twpage,text="Write a Tweet:")
	postlabel.pack()
	postlabel.configure(font=labelfont)
	postlabel.configure(background="#263238")
	postlabel.configure(foreground="#ffffff")
	hwadjust(postlabel)
	post = Text(twpage,height="1",width="8",font=inputfont)
	post.pack()
	post.focus_set()
	twbtn=Button(twpage,text="Login !",command=lambda:twitter(username,password,post))
	twbtn.pack()
	twbtn.configure(font=myfont)
	twbtn.configure(background="#2196f3")
	twbtn.configure(foreground="#ffffff")
	hwadjust(twbtn)

def facebookpageinit(page):
	facebookpage = Toplevel(page)
	usernamelabel = Label(facebookpage,text="Username / Mobile :")
	usernamelabel.pack()
	usernamelabel.configure(font=labelfont)
	usernamelabel.configure(background="#263238")
	usernamelabel.configure(foreground="#ffffff")
	username = Text(facebookpage,height="1",width="8",font=inputfont)
	username.pack()
	username.focus_set()
	#e.configure(foreground="WHITE")
	hwadjust(username)
	passwordlabel = Label(facebookpage,text="Password :")
	passwordlabel.pack()
	passwordlabel.configure(font=labelfont)
	passwordlabel.configure(background="#263238")
	passwordlabel.configure(foreground="#ffffff")
	password = Entry(facebookpage,font=inputfont,show="*")
	password.pack()
	password.focus_set()
	#e.configure(foreground="WHITE")
	#hwadjust(password)
	'''postlabel = Label(facebookpage,text="Write a post:")
	postlabel.pack()
	postlabel.configure(font=labelfont)
	postlabel.configure(background="#263238")
	postlabel.configure(foreground="#ffffff")
	post = Text(facebookpage,height="1",width="8",font=inputfont)
	post.pack()
	post.focus_set()'''
	fbbtn=Button(facebookpage,text="Login !",command=lambda:facebook(username,password))
	fbbtn.pack()
	fbbtn.configure(font=myfont)
	fbbtn.configure(background="#2196f3")
	fbbtn.configure(foreground="#ffffff")
	hwadjust(fbbtn)


def socialpage():
	newpagesc = Toplevel(m)
	fbpagelaunch=Button(newpagesc,text="Facebook",command=lambda:facebookpageinit(newpagesc))
	fbpagelaunch.pack()
	fbpagelaunch.configure(font=myfont)
	fbpagelaunch.configure(background="#2196f3")
	fbpagelaunch.configure(foreground="#ffffff")
	fseperator = Label(newpagesc,text=" ")
	fseperator.pack()
	fseperator.configure(font=myfont)
	#fseperator.configure(background="#263238")
	twpagelaunch=Button(newpagesc,text="Twitter",command=lambda:twitterpageinit(newpagesc))
	twpagelaunch.pack()
	twpagelaunch.configure(font=myfont)
	twpagelaunch.configure(background="#2196f3")
	twpagelaunch.configure(foreground="#ffffff")
	hwadjust(twpagelaunch)
	hwadjust(fbpagelaunch)
	fseperator = Label(newpagesc,text=" ")
	fseperator.pack()
	fseperator.configure(font=myfont)
	newsbtn=Button(newpagesc,text="Read the latest news",command=grabnews)
	newsbtn.pack()
	newsbtn.configure(font=myfont)
	newsbtn.configure(background="#2196f3")
	newsbtn.configure(foreground="#ffffff")
	hwadjust(newsbtn)


def aboutpageinit():
	aboutpage = Toplevel(m)
	aboutpage.configure(background="#263238")
	title = Label(aboutpage,text="Let Python Handle It !")
	title.configure(font=labelfont1)
	title.configure(background="#263238")
	title.configure(foreground="#ffffff")
	credits = Label(aboutpage,text="Credits")
	credits.configure(font=labelfont1)
	credits.configure(background="#263238")
	credits.configure(foreground="#ffffff")
	c1 = Label(aboutpage,text="Abhishek C. Gidde (T.E) (Computer Science)")
	c1.configure(font=labelfont1)
	c1.configure(background="#263238")
	c1.configure(foreground="#ffffff")
	c2 = Label(aboutpage,text="Janvi V. Saddi (T.E) (Computer Science)")
	c2.configure(font=labelfont1)
	c2.configure(background="#263238")
	c2.configure(foreground="#ffffff")
	c3 = Label(aboutpage,text="Harshal R. Patil (T.E) (Computer Science)")
	c3.configure(font=labelfont1)
	c3.configure(background="#263238")
	c3.configure(foreground="#ffffff")
	fseperator = Label(aboutpage,text=" ")
	fseperator.pack()
	fseperator.configure(font=myfont)
	contribute=Button(aboutpage,text="Contribute to our project @ GitHub",command=opengit)
	contribute.configure(font=myfont)
	contribute.configure(background="#2196f3")
	contribute.configure(foreground="#ffffff")
	hwadjust(contribute)
	title.pack()
	credits.pack()
	c1.pack()
	c2.pack()
	c3.pack()
	contribute.pack()
	    

def opengit():
	webbrowser.open("https://www.github.com/gidde-abhishek/lphi-let-python-handle-it")


def test(fromloc,mapdest):
	print(mapdest)
	print(fromloc)

def pushfiles():
	os.system("adb push C:/Users/abhis/Desktop/lphi/send /sdcard/lphireceived")
def pullfiles():
	os.system("adb pull /sdcard/lphisend C:/Users/abhis/Desktop/lphi/received")

def androidftpwininit(androidwin):
	androidftpwin = Toplevel(androidwin)
	giddetransfer=Button(androidftpwin,text="Click to send files to your device !",command=pushfiles)
	giddetransfer.pack()
	giddetransfer.configure(font=myfont)
	giddetransfer.configure(background="#2196f3")
	giddetransfer.configure(foreground="#ffffff")
	hwadjust(giddetransfer)
	giddetransfer=Button(androidftpwin,text="Click to receive files from your device !",command=pullfiles)
	giddetransfer.pack()
	giddetransfer.configure(font=myfont)
	giddetransfer.configure(background="#2196f3")
	giddetransfer.configure(foreground="#ffffff")
	hwadjust(giddetransfer)


def androidwidgets():
	androidwin = Toplevel(m)
	ocrbutton=Button(androidwin,text="Click to read your android screen !",command=ocr)
	ocrbutton.pack()
	ocrbutton.configure(font=myfont)
	ocrbutton.configure(background="#2196f3")
	ocrbutton.configure(foreground="#ffffff")
	hwadjust(ocrbutton)
	aftp=Button(androidwin,text="Android File Transfer",command=lambda:androidftpwininit(androidwin))
	aftp.pack()
	aftp.configure(font=myfont)
	aftp.configure(background="#2196f3")
	aftp.configure(foreground="#ffffff")
	hwadjust(aftp)
	




def popupgoogle():
   googleshopwindow = Toplevel(m)
   abby = Label(googleshopwindow,text="Type to start searching or shopping !")
   abby.pack()
   abby.configure(font=labelfont)
   abby.configure(background="#263238")
   abby.configure(foreground="#ffffff")
   #seperator(googleshopwindow)

   e = Text(googleshopwindow,height="1",width="8",font=inputfont)
   e.pack()
   e.focus_set()
   #e.configure(foreground="WHITE")
   hwadjust(e)
   #seperator(googleshopwindow)

   button = Button(googleshopwindow,text="Google",width=25,command=lambda:google(e))
   button.pack()
   button.configure(font=myfont)
   button.configure(background="#2196f3")
   button.configure(foreground="#ffffff")
   #seperator(googleshopwindow)

   button1 = Button(googleshopwindow,text="Shop",width=25,command=lambda:shop(e))
   button1.pack()
   button1.configure(font=myfont)
   button1.configure(background="#2196f3")
   button1.configure(foreground="#ffffff")
   #seperator(googleshopwindow)

def popupmap():
	directionswindow = Toplevel(m)
	maploc = Label(directionswindow,text="Set Start Location")
	maploc.pack()
	maploc.configure(font=inputfont)
	maploc.configure(background="#263238")
	maploc.configure(foreground="#ffffff")
	#seperator(directionswindow)
	fromloc = Text(directionswindow,height="1",width="8",font=inputfont)
	fromloc.pack()
	fromloc.focus_set()
	hwadjust(fromloc)
	#seperator(directionswindow)
	mapdest = Label(directionswindow,text="Set End Location")
	mapdest.pack()
	mapdest.configure(font=inputfont)
	mapdest.configure(background="#263238")
	mapdest.configure(foreground="#ffffff")
	#seperator(directionswindow)
	toloc = Text(directionswindow,height="1",width="8",font=inputfont)
	toloc.pack()
	toloc.focus_set()
	hwadjust(toloc)
	#seperator(directionswindow)
	locatebutton = Button(directionswindow,text="Get Directions !",width=25, command= lambda:locate(fromloc,mapdest))
	locatebutton.pack()
	locatebutton.configure(font=myfont)
	locatebutton.configure(background="#2196f3")
	locatebutton.configure(foreground="#ffffff")
	#seperator(directionswindow)

m = Tk()
m.configure(background="#263238")
queryy = StringVar()
m.title("LPHI - Let Python Handle It !")
#m.geometry("750x750")
m.resizable(width=False, height=False)

maintitle = Label(m,text="LET PYTHON HANDLE IT !")
maintitle.configure(font=labelfont1)
maintitle.configure(background="#263238")
maintitle.configure(foreground="#ffffff")
maintitle.pack()
seperator()

btntogooglewindow = Button(m,text="Search the web / Buy",command=popupgoogle)
hwadjust(btntogooglewindow)
btntogooglewindow.configure(font=myfont)
btntogooglewindow.configure(background="#2196f3")
btntogooglewindow.configure(foreground="#ffffff")
btntomapwindow = Button(m,text="Directions - look before you leave !",command=popupmap)
hwadjust(btntomapwindow)
btntomapwindow.configure(font=myfont)
btntomapwindow.configure(background="#2196f3")
btntomapwindow.configure(foreground="#ffffff")



ocrbutton=Button(m,text="Android Tools",command=androidwidgets)
ocrbutton.pack()
ocrbutton.configure(font=myfont)
ocrbutton.configure(background="#2196f3")
ocrbutton.configure(foreground="#ffffff")
hwadjust(ocrbutton)
#ocrbutton.configure(height=34)
#ocrbutton.configure(width=97)
seperator()
btntogooglewindow.pack() #placed after the tools button
seperator()
btntomapwindow.pack()
seperator()
socialpagebtn = Button(m,text="Social Login & Daily News",command=socialpage)
socialpagebtn.pack(side="left")
socialpagebtn.configure(font=myfont)
socialpagebtn.configure(background="#2196f3")
socialpagebtn.configure(foreground="#ffffff")
hwadjust(socialpagebtn)
socialpagebtn = Button(m,text="About the program",command=aboutpageinit)
socialpagebtn.pack(side="left")
hwadjust(socialpagebtn)
socialpagebtn.configure(font=myfont)
socialpagebtn.configure(background="#2196f3")
socialpagebtn.configure(foreground="#ffffff")


m.mainloop()
