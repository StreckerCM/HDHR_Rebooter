#!/usr/bin/python
# -*- coding: utf-8 -*-
# Copyright 2015-2016 Christopher Strecker

import os
import sys
import re
import time

def rebooter():
	#run hdhomerun_config discover

	description = (
	'Command line interface for rebooting SiliconDust '
	'HDHomeRun Devices.\n'
	'------------------------------------------------------------'
	'--------------\n'
	'https://github.com/StreckerCM/HDHR_Rebooter')


	sys.stdout.write('\r\n')

	print "Finding HDHomeRun Devices"
	sys.stdout.write('\r\n')
	result = os.popen("/usr/bin/hdhomerun_config discover").read()

	#split into lines
	lines = result.splitlines()

	for line in lines:
		words = re.split("\s+",line)
		if len(words) == 6:
	   		print "Rebooting HDHomeRun Device: " + words[2]
			os.system("hdhomerun_config " + words[2] + " set /sys/restart self")
		else:
			print "Error Identifying HDHomeRun"

	sys.stdout.write('\r\n')
	sys.stdout.write('Waiting for Devices to Restart')

	for i in xrange(0,20): 
		sys.stdout.write('.')
		time.sleep(1)
		sys.stdout.flush()

	sys.stdout.write('\r\n')
	sys.stdout.write('\r\n')

	print os.popen("/usr/bin/hdhomerun_config discover").read()

	print_('\nCompleted')

        return

def main():
	try:
		rebooter()
	except KeyboardInterrupt:
		print_('\nCancelling...')

if __name__ == '__main__':
        main()

