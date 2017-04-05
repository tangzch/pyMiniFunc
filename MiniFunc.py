#!/usr/bin/env python
# -*- coding: utf-8 -*-
#Filename:MiniFunc.py
 
# -*- coding: utf-8 -*-

import types
import json

#                      /\  /\      
#                    ( @ . @ )     
##################^^^#########^^^##
##       Regular expression      ##
#######################~..~########
#                                  
import re
def paramVerification(param):
	# param that including ONLY [a-z,A-Z,0-9,_] is legal.
	reStr = r'^\w+$'
	m = re.match(reStr, param)
	if m:
		return True
	else:
		return False
	
def paramSplit(reString, paramString):
	# return a param LIST, split by reString
	return re.split(reString, paramString)

#                      /\   /\     
#                 ╭╮(╯▽╰)╭╮ 
##################^^^#########^^^##
##      Encrypto Utilities       ##
#######################~..~########
#                                  
import hashlib
def md5(string):
	if type(string) is types.StringType:
		m = hashlib.md5()
		m.update(string)
		return m.hexdigest()
	else:
		return ''

#                      /\  /\     
#                    ψ(╰_╯)σ 
###################################
##         Log Utilities         ##
#######################~..~########
#                                  
import re
import logging  
def setLogConfig():
	logging.basicConfig(level=logging.WARNING,  
		filename='./Log/log.txt',  
		filemode='w',  
		format='%(asctime)s - %(filename)s[line:%(lineno)d] - %(levelname)s: %(message)s')
	pass
	
def Log(level, message):
	try:
		m = re.match(r'^warning$|^error$', level)
		if m:
			func = getattr(logging, level)
			func(message+'\n')
		else:
			print 'log level wrong!'
			logging.error('log level wrong: %s\n' %message)
	except Exception as e:
		logging.error('log exception: %s\n' %e.message)

#                     /\   /\      
#                 ╭(#￣▽￣#)╮ 
##################^^^#######^^^####
##          Time handler         ##
#######################~..~########
#                                  
import time
def getCurrentTime():
	# Time format: 20170301162559
	return time.strftime("%Y%m%d%H%M%S", time.localtime())

def getCurrentMKTime():
	# return time format: Sat Mar 28 22:24:24 2016
	return time.strftime("%a %b %d %H:%M:%S %Y", time.localtime())

def transStringToTime(timeString):
	# Time string format: Sat Mar 28 22:24:24 2016
	# return 1459175064.0
	return time.mktime(time.strptime(timeString,"%a %b %d %H:%M:%S %Y"))

#        (\   /)                   
#     ﹏(￣▽￣) ﹏                 
#####^^^########^^^################
##          QR  handler          ##
##########~..~#####################
#                                  
import qrcode
from PIL import Image
def make_QR(strQR):
	qr = qrcode.QRCode(  
		version=4,  
		error_correction=qrcode.constants.ERROR_CORRECT_L,  
		box_size=10,  
		border=4,  
	)  

	qr.add_data(str(strQR))  
	qr.make(fit=True)  
	img = qr.make_image()
	return img

#        (\   /)                   
#     ﹏(0▽ 0 ) ﹏                 
#####^^^########^^^################
##        Queue  handler         ##
##########~..~#####################
#                                  
import Queue
queue = Queue.Queue()
def addItem(item):
	queue.put(item)
	
def getItem():
	try:
		item = queue.get(timeout = 2)
		return item
	except Queue.Empty:
		print 'queue empty'
		return None
	
def getQSize():
	return queue.qsize()
	
def clearQueue():
	queue.queue.clear()

##############################################################################
# Ƹ̵̡Ӝ̵̨̄Ʒ Ƹ̵̡Ӝ̵̨̄Ʒ Ƹ̵̡Ӝ̵̨̄Ʒ Ƹ̵̡Ӝ̵̨̄Ʒ Ƹ̵̡Ӝ̵̨̄Ʒ Ƹ̵̡Ӝ̵̨̄Ʒ Ƹ̵̡Ӝ̵̨̄Ʒ Ƹ̵̡Ӝ̵̨̄Ʒ Ƹ̵̡Ӝ̵̨̄Ʒ Ƹ̵̡Ӝ̵̨̄Ʒ Ƹ̵̡Ӝ̵̨̄Ʒ Ƹ̵̡Ӝ̵̨̄Ʒ Ƹ̵̡Ӝ̵̨̄Ʒ Ƹ̵̡Ӝ̵̨̄Ʒ Ƹ̵̡Ӝ̵̨̄Ʒ Ƹ̵̡Ӝ̵̨̄Ʒ Ƹ̵̡Ӝ̵̨̄Ʒ Ƹ̵̡Ӝ̵̨̄Ʒ Ƹ̵̡Ӝ̵̨̄Ʒ 
#   Ƹ̵̡Ӝ̵̨̄Ʒ Ƹ̵̡Ӝ̵̨̄Ʒ Ƹ̵̡Ӝ̵̨̄Ʒ Ƹ̵̡Ӝ̵̨̄Ʒ Ƹ̵̡Ӝ̵̨̄Ʒ Ƹ̵̡Ӝ̵̨̄Ʒ Ƹ̵̡Ӝ̵̨̄Ʒ Ƹ̵̡Ӝ̵̨̄Ʒ Ƹ̵̡Ӝ̵̨̄Ʒ Ƹ̵̡Ӝ̵̨̄Ʒ Ƹ̵̡Ӝ̵̨̄Ʒ Ƹ̵̡Ӝ̵̨̄Ʒ Ƹ̵̡Ӝ̵̨̄Ʒ Ƹ̵̡Ӝ̵̨̄Ʒ Ƹ̵̡Ӝ̵̨̄Ʒ Ƹ̵̡Ӝ̵̨̄Ʒ Ƹ̵̡Ӝ̵̨̄Ʒ Ƹ̵̡Ӝ̵̨̄Ʒ   
##############################################################################

if '__main__' == __name__:
	#iStr = 'weixin://wxpay/bizpayurl?pr=c0LMOdd'
	#img = make_QR(iStr)
	#img.show()
	#112.74.171.209 "POST /FASTCODE?ID=6225504767&USERNAME=fanxiang&VMC=10571&PTYPE=FASTCODE&PID=810&FASTCODE=303&MAC=4ff162a9c27f18789204b2141a08c0b8
	#ss = 'ID=6225504767&USERNAME=fanxiang&PASSWORD=fanxiang8817&VMC=10571&PTYPE=FASTCODE&PID=810&FASTCODE=303'
	#print ss
	ss = 'QID=000005&USERNAME=ubox&PASSWORD=ubox123&QLEVEL=WARNING'
	#6372e9060cd23d1be2c04e2de3766439
	print md5(ss)
	#http://103.231.67.143:8079/QUERY?QID=001234&QLEVEL=SPECIFY&STARTTIME=20170329000000&ENDTIME=20170329235959&USERNAME=ubox&MAC=6372e9060cd23d1be2c04e2de3766439
	
	#setLogConfig()
	#count = 10
	#while(count):
	#	Log('warning','message 1')
	#	count -= 1
	
	#while(True):
	#	cType = raw_input("Input:")
	#	if cType == 'a':
	#		addItem("A")
	#	elif cType == 'g':
	#		print getItem()
	#	elif cType == 's':
	#		print getQSize()
	#	elif cType == 'c':
	#		clearQueue()
	#	else:
	#		break;
	#	pass





