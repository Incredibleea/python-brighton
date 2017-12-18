#!/bin/bash

function HELP
{
	echo -e "\nusage: eyeCustomiser.sh [-h] [-i] [-c] [TEMP]\n\nThis script customise display's colors temperature according to time.\n\n\
	\rpositional arguments:\n TEMP\t\tvalue of the color temperature [1000-10000], not applicable in initial mode\n\n\
	\roptional arguments:\n -h, --help\tshow this help message and exit\n\
	\r -i, --initial\trun script in initial mode, add crontab jobs\n\
	\r -c, --calc\tcalculate current color temperature\n\
	\r -q, --disable\tdisable EyeCustomiser\n\
	\n\r@libraries: it is recommended, but not necessary to get redshift program\n\
	\n\n@NOTE: This script is part of EyeCare program.\n"
}

function calcAndSet()
{
	CURR_TIME=$CURR_HOUR$CURR_MINUTE
	SET_TIME=$SET_HOUR$SET_MINUTE
	RISE_TIME=$RISE_HOUR$RISE_MINUTE
	if [[ $CURR_TIME -le $SET_TIME ]] && [[ $CURR_TIME -ge $RISE_TIME ]]; then
		eyeCustomiser 6500
	else
		eyeCustomiser 4500
	fi
}

function eyeCustomiser()
{
	local COLOR_TEMP=$1
	PARENT_DIR=$(dirname "$DIR")
	TMP="$($PARENT_DIR/lib/sct $COLOR_TEMP &>/dev/null)"						# check if sct.c program is available
	SCT_ERR=$?
	if [[ `dpkg -s redshift &>/dev/null` ]]; then								# check if redshift is installed
		echo `redshift -O $COLOR_TEMP` 1>/dev/null
	elif [[ $SCT_ERR -eq 0 ]]; then
		echo `$PARENT_DIR/lib/sct $COLOR_TEMP` 1>/dev/null
	else																		# out of libraries
		for monitor in "${MONITOR[@]}"; do
			echo "Program redshift and program sct are not available. Using basic xrandr."
			echo `xrandr --output $monitor --brightness 0.8` 1>/dev/null
		done
	fi
}

function setConstants()
{
	PARENT_DIR=$(dirname "$DIR")
	SUN_PARAM=`python ./src/SunParameters.py`
	echo $SUN_PARAM | grep -q -e "^[0-9][0-9]:[0-9][0-9] [0-9][0-9]:[0-9][0-9]$"
	if [ $? != 0 ]; then
		SUN_PARAM="07:00 17:00"
	fi
	RISE_HOUR=`echo $SUN_PARAM | cut -d " " -f 1 | cut -d ":" -f 1`
	RISE_MINUTE=`echo $SUN_PARAM | cut -d " " -f 1 | cut -d ":" -f 2`
	SET_HOUR=`echo $SUN_PARAM | cut -d " " -f 2 | cut -d ":" -f 1`
	SET_MINUTE=`echo $SUN_PARAM | cut -d " " -f 2 | cut -d ":" -f 2`
	CURR_HOUR=(`date +%H`)
	CURR_MINUTE=(`date +%M`)
}

function setEyeCustomiser()
{
	disableEyeCustomiser
	calcAndSet
	(crontab -l -u $USER; echo "$SET_MINUTE $SET_HOUR * * * export DISPLAY="$dis" && $DIR/eyeCustomiser.sh 4500") | crontab -u $USER - 1>/dev/null
	(crontab -l -u $USER; echo "$RISE_MINUTE $RISE_HOUR * * * export DISPLAY="$dis" && $DIR/eyeCustomiser.sh 6500") | crontab -u $USER - 1>/dev/null
}

function disableEyeCustomiser()
{
	echo `crontab -l -u $USER 2>/dev/null | grep -v "eyeCustomiser.sh" | crontab -u $USER -` 1>/dev/null
	eyeCustomiser 6500
	for monitor in "${MONITOR[@]}"; do
		echo `xrandr --output $monitor --brightness 1.0` 1>/dev/null
	done
}

DIR="$(cd -- "$(dirname "$0")" && pwd)"
declare MONITOR=($($DIR/scanDisplay.sh))
export XAUTHORITY=/home/$USER/.Xauthority
dis=$DISPLAY
export DISPLAY=$dis

if [ "$1" == "-h" ] || [ "$1" == "--help" ]; then
	HELP
	exit 0
elif [ "$1" == "-q" ] || [ "$1" == "--disable" ]; then
	eyeCustomiser 6500
	disableEyeCustomiser
elif [ "$1" == "-i" ] || [ "$1" == "--initial" ]; then
	setConstants
	setEyeCustomiser
elif [ "$1" == "-c" ] || [ "$1" == "--calc" ]; then
	setConstants
	calcAndSet
else
	if [[ $1 -ge 1000 ]] && [[ $1 -le 10000 ]]; then
		eyeCustomiser $1
	else																	# default value applicable only in manual call
		eyeCustomiser 6500
	fi
fi
