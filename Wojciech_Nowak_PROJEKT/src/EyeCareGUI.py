#!/usr/bin/python
# -*- coding: iso-8859-2 -*-

from Tkinter import *
import os
import subprocess
import tkMessageBox

DIR = os.path.abspath(os.path.dirname(sys.argv[0]))

class EyeCareGUI:

	def setEyeBreakerType(self, event):
		self.button_eb.configure(text="ON")
		os.system(DIR + "/EyeCare.py --eyebreaker " + self.entry_eb.get())

	def setEyeBreaker(self, event):
		if str(self.button_eb.configure('text')[-1]) == "OFF":
			os.system(DIR + "/EyeCare.py --eyebreaker")
			self.button_eb.configure(text="ON")
		else:
			subprocess.call(DIR + '/src/eyeBreaker.sh --disable',shell=True)
			self.entry_eb.delete(first=0,last=10)
			self.button_eb.configure(text="OFF")

	def setEyeCustomiser(self, event):
		if str(self.button_ec.configure('text')[-1]) == "OFF":
			os.system(DIR + "/EyeCare.py --eyecustomiser")
			self.button_ec.configure(text="ON")
		else:
			subprocess.call(DIR + '/src/eyeCustomiser.sh --disable',shell=True)
			self.button_ec.configure(text="OFF")

	def eyeCustomiser(self, event):
		subprocess.call(DIR + '/src/eyeCustomiser.sh ' + self.entry_sct.get(),shell=True)

	def disableEyeCare(self):
		os.system(DIR + "/EyeCare.py --disable")
		self.button_ec.configure(text="OFF")
		self.button_ec.configure(text="OFF")
		self.entry_sct.delete(first=0,last=20)
		self.entry_sct.insert(END,'color temperature')
		self.entry_sct.configure(fg='grey')
		self.entry_eb.delete(first=0,last=20)
		self.entry_eb.insert(END,'55')

	def prepareEntry(self, event):
		self.entry_sct.delete(first=0,last=20)
		self.entry_sct.configure(fg='black')

	def printHelp(event):
		tkMessageBox.showinfo("help", "\rEyeBreaker module will take care of your eyes' physical condition \
	\rby performing notification every MINUTES. By this notification try to look around you \
	\rand find green things to give your eyesight a rest. \
	\rIf you want to change Period time please turn off module first.\n\
	\rEyeCustomiser module will take care of your eyes after sunset. \
	\rEyeCustomiser downloads sunrise and sunset time to set your screen colors temperature \
	\rappriopriate to the current time.\n\
	\rYou can also set display color temperature manually basing on current light conditions. \
	\rThe value should be placed into entry box and approved by pressing \"Return\" key or \
	\rby pressing \"Set\" button. \
	\rThe range of values is <1000,10000> Kelvin. Default system value is 6500K.\
	\rThe higher value the coolest color temperature.\n\
	\rTroubleshooting: type \'crontab -l\' in terminal to show current Cron jobs. \
	\rIt should look like this: \n\
	\rEyeBreaker enabled:\
	\r*/55 * * * * PATH/Wojciech_Nowak_2_PROJEKT/eyeBreaker.sh\
	\rEyeCustomiser enabled: \
	\r15 17 * * * PATH/Wojciech_Nowak_2_PROJEKT/eyeCustomiser.sh 4500\
	\r33 06 * * * PATH/Wojciech_Nowak_2_PROJEKT/eyeCustomiser.sh 6500\
")

	def __init__(self,master):
		frame = Frame(master)
		frame.pack()

		self.label_eb = Label(frame, text="EyeBreaker")
		self.label_eb.grid(row=1, sticky=E)
		self.label_eb2 = Label(frame, text="Period between notifications")
		self.label_eb2.grid(row=0, column=1)
		self.entry_eb = Entry(frame, justify=CENTER)
		self.entry_eb.insert(END,'55')
		self.entry_eb.grid(row=1, column=1)
		self.entry_eb.bind("<Return>",self.setEyeBreakerType)
		self.button_eb=Button(frame, text="OFF")
		self.button_eb.grid(row=1,column=2)
		self.button_eb.bind("<Button-1>",self.setEyeBreaker)

		self.label_ec = Label(frame, text="EyeCustomiser")
		self.label_ec.grid(row=3, sticky=E)
		self.button_ec=Button(frame, text="OFF")
		self.button_ec.grid(row=3,column=2)
		self.button_ec.bind("<Button-1>",self.setEyeCustomiser)

		self.label_sct = Label(frame, text="Set color temperature")
		self.label_sct.grid(row=4)
		self.entry_sct = Entry(frame, justify=CENTER, fg='grey')
		self.entry_sct.insert(END,'color temperature')
		self.entry_sct.bind("<Return>",self.eyeCustomiser)
		self.entry_sct.bind("<Button-1>",self.prepareEntry)
		self.entry_sct.grid(row=4, column=1)
		self.button_sct = Button(frame, text="Set")
		self.button_sct.bind("<Button-1>",self.eyeCustomiser)
		self.button_sct.grid(row=4, column=2, sticky=W)

		self.button_dec = Button(frame, text="Disable EyeCare", fg='red', command=self.disableEyeCare)
		self.button_dec.grid(row=5,columnspan=3)

		self.button_dec = Button(frame, text="?", bg='yellow', fg='black', command=self.printHelp)
		self.button_dec.grid(row=5,column=3)

def initializeEyeCareGUI():
	root = Tk()
	root.title("EyeCare")
	root.option_add("*Dialog.msg.wrapLength", "650")

	ECgui = EyeCareGUI(root)

	root.mainloop()
