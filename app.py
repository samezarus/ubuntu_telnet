#!/usr/bin/env python3
# coding: utf-8

import telnetlib
import time
import datetime
import os

# --------------------------------------------------------------------------------------------
def testLogFolder(log_folder):
	if (not os.path.exists(log_folder)):
		os.makedirs(log_folder)

def createDayFolder(log_folder):
	day_folder = log_folder+str(datetime.datetime.now().date())
	if (not os.path.exists(day_folder)):
		os.makedirs(day_folder)
	return day_folder

def createDayFile(log_folder):
	day_file = log_folder+str(datetime.datetime.now().date()) + '.log'
	return day_file

# --------------------------------------------------------------------------------------------

port = 2300
host = '172.16.17.2'
user = 'smdr'
password = 'pccsmdr'

log_folder = '/var/log/ats_loger/'

telnet = telnetlib.Telnet()
telnet.open(host, port)

telnet.read_until('-'.encode('ascii'))
telnet.write(user.encode('ascii') + b'\r')

telnet.read_until('Enter Password:'.encode('ascii'))
telnet.write(password.encode('ascii') + b"\r")

#day_folder_path = createDayFolder(log_folder) +'/log.txt'
day_file_name = createDayFile(log_folder)

while True:
	time.sleep(1)

	s = str(telnet.read_very_eager())
	if (s != '' and s != "b''"):
		day_file = open(day_file_name, '+a')
		day_file.write(s)
		day_file.close()
		#print(s)
	s = ''