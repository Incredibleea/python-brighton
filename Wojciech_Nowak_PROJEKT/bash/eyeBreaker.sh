#!/bin/bash

function HELP
{	
	echo -e "\nusage: eyeBreaker.sh [-h] [-i PERIOD]\n\nThis script performs notification for every PERIOD minutes of work.\n\n\
	\rpositional arguments:\n TEMP\t\tvalue of the color temperature [1000-10000], not applicable in initial mode\n\n\
	\roptional arguments:\n -h, --help\tshow this help message and exit\n\
	\r -i, --initial\turn script in initial mode, add crontab jobs\
	\r -q, --disable\tdisable EyeBreaker\n\
	\rlibraries:\n it is recommended, but not necessary to get redshift program\n\
	\n\n@NOTE: This script is part of EyeCare program.\n"
}

function eyeBreaker()
{
	CURR_BRIGHTNESS=`xrandr --verbose --current|grep Brightness | cut -d ":" -f 2`
	for i in $(seq $CURR_BRIGHTNESS -0.01 0); do
		for monitor in "${MONITOR[@]}"; do
			xrandr --display $DISPLAY --output $monitor --brightness $i
			sleep 0.01
		done
	done
	# SLIDESHOW
	for i in $(seq 0 0.01 $CURR_BRIGHTNESS); do
		for monitor in "${MONITOR[@]}"; do
			xrandr --display $DISPLAY --output $monitor --brightness $i
			sleep 0.01
		done
	done
	echo `$DIR/eyeCustomiser.sh -c`												# bugfix: change into old color temp value
}

function setEyeBreaker()														# function adds entries in crontab jobs list
{
	disableEyeBreaker
	local PERIOD=$1
	(crontab -l -u $USER 2>/dev/null; echo "*/$PERIOD * * * * export DISPLAY="$dis" && $DIR/eyeBreaker.sh") | crontab -u $USER -
}

function disableEyeBreaker()
{
	echo `crontab -l -u $USER &>/dev/null | grep -v "eyeBreaker.sh" | crontab -u $USER -` 1>/dev/null
}

DIR="$(cd -- "$(dirname "$0")" && pwd)"
declare MONITOR=($($DIR/scanDisplay.sh))
export XAUTHORITY=/home/$USER/.Xauthority
dis=$DISPLAY
export DISPLAY="$dis"

if [ "$1" == "-h" ] || [ "$1" == "--help" ]; then
	HELP
	exit 0
elif [ "$1" == "-q" ] || [ "$1" == "--disable" ]; then
	disableEyeBreaker
elif [ "$1" == "-i" ] || [ "$1" == "--initial" ]; then
	if [[ $2 -ge 1 ]] && [[ $2 -le 59 ]]; then
		setEyeBreaker $2
	else
		setEyeBreaker 55
	fi
else
	eyeBreaker
fi