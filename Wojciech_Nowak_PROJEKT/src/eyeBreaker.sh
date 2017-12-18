#!/bin/bash

function HELP
{
	echo -e "\nusage: eyeBreaker.sh [-h][-q][-i PERIOD]\n\nThis script performs notification for every PERIOD minutes of work.\n\n\
	\rpositional arguments:\n PERIOD\t\ttime between notifications\n\n\
	\roptional arguments:\n -h, --help\tshow this help message and exit\n\
	\r -i, --initial\trun script in initial mode, add crontab jobs\n\
	\r -q, --disable\tdisable EyeBreaker\n\
	\n\r@libraries: it is recommended, but not necessary to get redshift program\n\
	\n@NOTE: This script is part of EyeCare program.\n"
}

function eyeBreaker()
{
	CURR_BRIGHTNESS=`xrandr --verbose --current|grep Brightness | cut -d ":" -f 2`
	echo $CURR_BRIGHTNESS
	for i in $CURR_BRIGHTNESS-0.1 $CURR_BRIGHTNESS-0.2 $CURR_BRIGHTNESS-0.3 $CURR_BRIGHTNESS-0.4 $CURR_BRIGHTNESS-0.5 0 ; do
		for monitor in "${MONITOR[@]}"; do
			xrandr --display $DISPLAY --output $monitor --brightness $i
			sleep 0.01
		done
	done
	# SLIDESHOW
	for i in 0 $CURR_BRIGHTNESS-0.4 $CURR_BRIGHTNESS-0.3 $CURR_BRIGHTNESS-0.2 $CURR_BRIGHTNESS-0.1 $CURR_BRIGHTNESS; do
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
