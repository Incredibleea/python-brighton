#!/usr/bin/python
# -*- coding: iso-8859-2 -*-

import sys
import os 			# directory path
import argparse
import subprocess	# running bash script

DIR = os.path.abspath(os.path.dirname(sys.argv[0]))
sys.path.append(DIR + '/src')


parser = argparse.ArgumentParser(description='This is EyeCare, program which takes care of your Eyes.', epilog="\
	\rlibraries:\n it is necessary for GUI purposes to get python-tk package\n")
parser.add_argument("-f", "--fast", help=" Use default options for all arguments and turn on all functionalities.\
	This option is major.", action="store_true")
parser.add_argument("-g", "--gui", help=" Run EyeCare with Graphical User Interface.\
	This option is major except --fast and --disable options", action="store_true")
parser.add_argument("-b", "--eyebreaker", help=" Turn on EyeBreaker module.\
	EyeBreaker module will take care of your eyes' physical condition \
	by performing notification every MINUTES. By this notification try to look around you\
	and find green things to give your eyesight a rest.", type=int, nargs='?', const=55, metavar="MINUTES")
parser.add_argument("-c", "--eyecustomiser", help=" Turn on EyeCustomiser module.\
	EyeCustomiser module will take care of your eyes after sunset.\
	EyeCustomiser downloads sunrise and sunset time to set your screen colors temperature\
	appriopriate to the current time.", action="store_true")
parser.add_argument("-q", "--disable", help=" Disable EyeCare on your computer.\
	This option is major except --fast option.", action="store_true")

args = parser.parse_args()

available = str(os.getenv('DISPLAY', 0))
if available == "0":
	print ("Currently you don't have any active graphical environment, so there is no sense to use this program.")
else:
	if args.fast == True:
		subprocess.call(DIR + '/bash/eyeBreaker.sh -i ',shell=True)
		subprocess.call(DIR + '/bash/eyeCustomiser.sh -i',shell=True)
	else:
		if args.disable == True:
			subprocess.call(DIR + '/bash/eyeCustomiser.sh --disable',shell=True)
			subprocess.call(DIR + '/bash/eyeBreaker.sh --disable',shell=True)
		else:
			if args.gui == True:
				try:
					from EyeCareGUI import initializeEyeCareGUI
 					import Tkinter
				except ImportError, e:
 					print ("Lacking package pytkon-tk is required to run GUI.")
 					raise SystemExit
				initializeEyeCareGUI()
			else:
				if args.eyebreaker >= 1:
					subprocess.call(DIR + '/bash/eyeBreaker.sh -i ' + str(args.eyebreaker),shell=True)
				if args.eyecustomiser == True:
					subprocess.call(DIR + '/bash/eyeCustomiser.sh -i',shell=True)
				else:
					print ("No options selected, type python EyeCare.py -h to print help")
