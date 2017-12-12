#!/bin/bash

function HELP
{	
	echo -e "\nusage: scanDisplay.sh [-h]\n\nThis script returns all connected display devices.\n\n\
	\roptional arguments:\n -h, --help  show this help message and exit\n\n@NOTE: This script is part of EyeCare program.\n"
}

dis=$DISPLAY

export XAUTHORITY=/home/$USER/.Xauthority
export DISPLAY=$dis

if [ "$1" == "-h" ] || [ "$1" == "--help" ]; then
	HELP
	exit 0
else
	__resultvar=($(xrandr -q | grep " connected" | cut -d" " -f 1))
	for name in ${__resultvar[*]}
	do
		echo $name
	done	
fi