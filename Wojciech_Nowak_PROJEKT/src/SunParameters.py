#!/usr/bin/python
# -*- coding: iso-8859-2 -*-

import urllib
import datetime
from bs4 import BeautifulSoup as bs

class SunParameters:
    """Class SunParameters has two methods:
    String: getSunrise()\t\treturns today's sunrise time in Cracow,
    String: getSunset()\t\t\treturns today's sunset time in Cracow.
	\r\nRequirements:\nIt is neccessary to have Internet connection to make this script runs correctly.
    \rIn case of no Internet connection default value will be returned (sunrise = 7:00, sunset = 17:00).
	\r\nNOTE: This script is part of EyeCare program.\n"""

    lines = []
    errFlag = False
    def __init__(self):
        URL = "http://pl.365.wiki/world/poland/krakow/sun/today/"
        try:
            content = urllib.urlopen(URL).read()
            soup = bs(content, 'html.parser')
            spans = soup.find_all('span', {'class' : 'value'})
            self.lines = [span.get_text() for span in spans]
        except IOError:
            print("There is no network connection, using default values (sunrise = 7:00, sunset = 17:00)")
            self.errFlag = True

    def getSunrise(self):
        if self.errFlag == True:
            return "7:00"
        else:
            time = self.lines[0].split(':', 1)
            sunrise = str(int(time[0]) - 1) + ':' + time[1]
            return sunrise
    def getSunset(self):
        if self.errFlag == True:
            return "17:00"
        else:
            time = self.lines[2].split(':', 1)
            sunset = str(int(time[0]) - 1) + ':' + time[1]
            return sunset
    def getSunParam(self):
        rise = self.getSunrise()
        sets = self.getSunset()
        return rise + ' ' + sets + '\n'

if __name__ == "__main__":
    SunParameters().getSunParam()
