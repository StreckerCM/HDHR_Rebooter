#!/usr/bin/python
# -*- coding: utf-8 -*-
# Copyright 2015-2016 Christopher Strecker
from __future__ import print_function

import os
import re
import sys
import getopt
import time
import signal

__version__ = '0.1.0'

# global variables
wait_time = 30
help = """usage: speedtest-cli 

Command line utility for rebooting all HDHomeRun Devices on your network
--------------------------------------------------------------------------
https://github.com/StreckerCM/HDHR_Rebooter

optional arguments:
\t-h, --help\t\tshow this help message and exit
\t-w, --wait\t\tchange the default reboot wait time (Default 30 seconds)
"""



def main():

	global help, wait_time

	#print 'ARGV      :', sys.argv[1:]
	
	try:
		options, remainder = getopt.getopt(sys.argv[1:], 'hw:', ['wait='])
	except Exception:
		pass
		
	#print 'OPTIONS   :', options
	
	for opt, arg in options:
		if opt in ('-h', '--help'):
			print(help)
			sys.exit()
		elif opt in ('-w', '--wait'):
			wait_time = int(arg)
      
	try:
		hddr_rebooter()
		print('Completed')
	except KeyboardInterrupt:
		print('Cancelling...')
		
def hddr_rebooter():
	#run hdhomerun_config discover
	
	global wait_time

	sys.stdout.write('\r\n')

	print('Finding HDHomeRun Devices')
	
	devlst = get_device_list()

	sys.stdout.write('\r\n')
	
	if len(devlst) == 0:
		print('ERROR: No HDHomeRun Devices Found')
		sys.stdout.write('\r\n')
		return
	
	for deviceid in devlst:
		print('Rebooting HDHomeRun device ID: ' + deviceid)
		os.system('hdhomerun_config ' + deviceid + ' set /sys/restart self')

	sys.stdout.write('\r\n')
	
	for i in xrange(0, wait_time + 1): 
		txtTime = str(wait_time - i)
		print('Waiting ' + txtTime.rjust(len(str(wait_time))) + 's for Devices to Restart', end='\r')
		sys.stdout.flush()
		if i > 0:
			time.sleep(1)

	sys.stdout.write('\r\n')
	sys.stdout.write('\r\n')
	
	print(os.popen('hdhomerun_config discover').read())
	
def get_device_list():

	devlst = []
	
	result = os.popen('hdhomerun_config discover').read()
	
	#split into lines
	lines = result.splitlines()
	
	for line in lines:
		words = re.split("\s+",line)
		if len(words) == 6:
			devlst.append(words[2])
		
	return devlst
	
if __name__ == '__main__':
	main()