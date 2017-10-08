#!/usr/bin/env python
# -*- coding: utf-8 -*-
#Filename:MiniFunc.py
 
# BY: Jason Tang @jetinno

import types
import json
import urllib
import urllib2
import requests

#                      /\  /\      
#                    ( @ . @ )     
##################^^^#########^^^##
##         Dict traverse         ##
#######################~..~########
#                       (          
def dictTraverse(DICT):
	for (k,v) in  DICT.items(): 
		print "DICT[%s]=" % k,v

def dictTraverse2(DICT):
	for k,v in DICT.iteritems(): 
		print "dict[%s]=" % k,v
		

#                      /\  /\      
#                    ( @ . @ )     
##################^^^#########^^^##
##       Regular expression      ##
#######################~..~########
#                       (          
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
#                        )          
import hashlib
import base64
def md5(string):
	if type(string) is types.StringType:
		m = hashlib.md5()
		m.update(string)
		return m.hexdigest()
	else:
		return ''

def sha256(string):
	if type(string) is types.StringType:
		m = hashlib.sha256()
		m.update(string)
		return m.hexdigest()
	else:
		return ''

def base64Encode(plainText):
	return base64.b64encode(plainText)
	
def base64Decode(Cipher):
	return base64.b64decode(Cipher)

def get_randomStr():
	import random
	import string
	chars = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
	return string.join(random.sample(chars,16)).replace(" ","")

#                      /\  /\     
#                    ψ(╰_╯)σ 
###################################
##         Log Utilities         ##
#######################~..~########
#                                  
import re
import logging  
def setInfoLogConfig():
	logging.basicConfig(level=logging.INFO,  
		filename='./Log/msgLog.txt',  
		filemode='w',  
		format='%(asctime)s - %(filename)s[line:%(lineno)d] - %(levelname)s: %(message)s')
	pass

def Log(level, message):
	try:
		m = re.match(r'^warning$|^error$|^info$', level)
		if m:
			func = getattr(logging, level)
			func(message)
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
#           \                      
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

#                     /\   /\      
#                 ╭(#￣▽￣#)╮ 
##################^^^#######^^^####
##          File handler         ##
#######################~..~########
#                                  
def readFile(filename):
	file_object = open(filename,'r')
	try:
		all_the_text = file_object.read( )
	finally:
		file_object.close( )
		return all_the_text
		
def readFileLines(filename):
	file_object = open(filename)
	try:
		list_of_all_the_lines = file_object.readlines( )
	finally:
		file_object.close( )
		return list_of_all_the_lines

def writeFile(filename, text):
	file_object = open(filename,'a+')
	try:
		file_object.write(text)
	finally:
		file_object.close( )
		
def writeFileLines(filename, list_of_lines):
	file_object = open(filename,'a+')
	try:
		file_object.writelines(list_of_lines)
	finally:
		file_object.close( )

#        (\   /)                   
#     ﹏(￣▽￣) ﹏                 
#####^^^########^^^################
##         math                  ##
##########~..~#####################
#                                  
import math
PI = 3.1415926535
def distance(Pa,Pb):
	return math.sqrt((Pa[0]-Pb[0])**2 + (Pa[1]-Pb[1])**2)

def sinA(AB,AC,BC):
	cosA = (AB**2 + AC**2 - BC**2) / (2*AB*AC)
	sinA = math.sqrt(1 - cosA**2)
	#print sinA
	return sinA

def square(Pa,Pb,Pc):
	AB = distance(Pa,Pb)
	AC = distance(Pa,Pc)
	BC = distance(Pb,Pc)
	#print AB,AC,BC,sinA(AB,AC,BC)
	S = AB * AC * sinA(AB,AC,BC) / 2
	#print round(S,2)
	return S

#        (\   /)                   
#     ﹏(0▽ 0 ) ﹏                 
#####^^^########^^^################
##          Curl  module         ##
##########~..~#####################
#                                  
import pycurl
import StringIO
def postXmlSSL(xml, url, second=6, cert=False, post=True):
	curl = pycurl.Curl()
	curl.setopt(pycurl.URL, url)
	curl.setopt(pycurl.TIMEOUT, second)
	curl.setopt(pycurl.SSL_VERIFYPEER,False)
	curl.setopt(pycurl.SSL_VERIFYHOST,False)
	#curl.setopt(pycurl.HTTPHEADER, '')
	#if cert:
	#	self.curl.setopt(pycurl.SSLKEYTYPE, "PEM")
	#	self.curl.setopt(pycurl.SSLKEY, WxPayConf_pub.SSLKEY_PATH)
	#	self.curl.setopt(pycurl.SSLCERTTYPE, "PEM")
	#	self.curl.setopt(pycurl.SSLCERT, WxPayConf_pub.SSLCERT_PATH)
	
	if post:
		curl.setopt(pycurl.POST, True)
		curl.setopt(pycurl.POSTFIELDS, xml)
	buff = StringIO.StringIO()
	curl.setopt(pycurl.WRITEFUNCTION, buff.write)

	curl.perform()
	return buff.getvalue()
	

# xml <---> json
def ToXml(paramDict):
	xml = "<xml>"
	for key,val in paramDict.items():
		if isinstance(val,int) or isinstance(val,long):
			xml += "<" + key + ">" + str(val) + "</" + key + ">"
		else:
			xml += "<" + key + "><![CDATA[" + str(val) + "]]></" + key +">"
		
	xml += "</xml>"
	return xml

def FromXml(xmlStr):
	import xmltodict
	paramDict = xmltodict.parse(xmlStr)
	return paramDict['xml']
	
	
##############################################################################
# Ƹ̵̡Ӝ̵̨̄Ʒ Ƹ̵̡Ӝ̵̨̄Ʒ Ƹ̵̡Ӝ̵̨̄Ʒ Ƹ̵̡Ӝ̵̨̄Ʒ Ƹ̵̡Ӝ̵̨̄Ʒ Ƹ̵̡Ӝ̵̨̄Ʒ Ƹ̵̡Ӝ̵̨̄Ʒ Ƹ̵̡Ӝ̵̨̄Ʒ Ƹ̵̡Ӝ̵̨̄Ʒ Ƹ̵̡Ӝ̵̨̄Ʒ Ƹ̵̡Ӝ̵̨̄Ʒ Ƹ̵̡Ӝ̵̨̄Ʒ Ƹ̵̡Ӝ̵̨̄Ʒ Ƹ̵̡Ӝ̵̨̄Ʒ Ƹ̵̡Ӝ̵̨̄Ʒ Ƹ̵̡Ӝ̵̨̄Ʒ Ƹ̵̡Ӝ̵̨̄Ʒ Ƹ̵̡Ӝ̵̨̄Ʒ Ƹ̵̡Ӝ̵̨̄Ʒ 
#   Ƹ̵̡Ӝ̵̨̄Ʒ Ƹ̵̡Ӝ̵̨̄Ʒ Ƹ̵̡Ӝ̵̨̄Ʒ Ƹ̵̡Ӝ̵̨̄Ʒ Ƹ̵̡Ӝ̵̨̄Ʒ Ƹ̵̡Ӝ̵̨̄Ʒ Ƹ̵̡Ӝ̵̨̄Ʒ Ƹ̵̡Ӝ̵̨̄Ʒ Ƹ̵̡Ӝ̵̨̄Ʒ Ƹ̵̡Ӝ̵̨̄Ʒ Ƹ̵̡Ӝ̵̨̄Ʒ Ƹ̵̡Ӝ̵̨̄Ʒ Ƹ̵̡Ӝ̵̨̄Ʒ Ƹ̵̡Ӝ̵̨̄Ʒ Ƹ̵̡Ӝ̵̨̄Ʒ Ƹ̵̡Ӝ̵̨̄Ʒ Ƹ̵̡Ӝ̵̨̄Ʒ Ƹ̵̡Ӝ̵̨̄Ʒ   
##############################################################################

def dictSort():
	import urllib
	paramDict = {}
	paramDict['orderNo'] = '55f232dd2e7b3cbfdb43f3d66733f3qq'
	
	paramDict['remark'] = 33333
	paramDict['mountStr'] = 0.01
	paramDict['returnURL'] = 'qwer'
	paramDict['productName'] = 102
	paramDict['isChangeUrl'] = 'true'
	paramDict['clickBackUrl'] = 'abcd'
	
	#paramDict['salt'] = '123456789'
	
	paramDict['cerName'] = 'tianjin_dingnuo'
	paramDict['date'] = getCurrentTime()[0:8]
	paramDict['key'] = 'VQXMUFKYRDYAHEVTSOQLIJIZWCWNISUAEUBEFODNKCPZIYZBPR'

	sortedList = sorted(paramDict.iteritems(), key=lambda asd:asd[0], reverse = False)
	paramStr = urllib.urlencode(sortedList)
	print paramStr
	sign = md5(paramStr).upper()
	print sign

	paramDict['sign'] = sign
	return paramDict

def isIPAddr(ipAddrStr):
	if not ipAddrStr:
		return False
	
	SegmentList = ipAddrStr.split('.')
	if not SegmentList[0].isdigit() or int(SegmentList[0]) not in range(1,256):
		return False
	
	for idx in range(1,4):
		if not SegmentList[idx].isdigit() or int(SegmentList[idx]) not in range(0,256):
			return False
	
	return True
	

def param_verify(param):
	goodList = 'abcdefghijklmnopqrstuvwxyz0123456789_'
	paramStr = str(param).lower();
	
	tagList = param.split('_')
	if len(tagList)>1:
		if tagList[1][:3] == 'sub':
			return False
	
	reCode = True
	for c in paramStr:
		if not c in goodList:
			reCode = False
			break;
	return reCode
	
	#cerName=tianjin_dingnuo&clickBackUrl=xxx&date=20170427&isChangeUrl=false&key=VQXMUFKYRDYAHEVTSOQLIJIZWCWNISUAEUBEFODNKCPZIYZBPR&mountStr=0.01&orderNo=55f232dd2e7b3cbfdb43f3d66733f3a1&productName=103&remark=33333&returnURL=xxx
	#faa57d21c51dd15b91195c854e9312ae

def sort_list(list):
	return sorted(list)
	
def packHeader(bodyLen):
	msgLen = bodyLen + 12
	headerStr = ''
	count = 4
	while count:
		char = msgLen & 0xff
		char += ord('0')
		msgLen >>= 8
		if char > 255:
			char -= 256
			msgLen += 1
		pass
		headerStr += chr(char) 
		count -= 1
	headerStr += '00000000'
	return headerStr
	
def get_signStr(paramList):
	str4Sign=''
	for item in paramList:
		str4Sign += str(item[0]) + '=' + str(item[1]) + '&'
	return str4Sign
	
def packHeader(bodyLen):
	msgLen = bodyLen + 12
	headerStr = ''
	count = 4
	while count:
		char = msgLen & 0xff
		char += ord('0')
		msgLen >>= 8
		if char > 255:
			char -= 256
			msgLen += 1
		pass
		headerStr += chr(char) 
		count -= 1
	headerStr += '00000000'
	return headerStr
	
if '__main__' == __name__:
	#order_no = "123456789012345612457802"
	#qr = doABCCharge(order_no,33333,1,810)
	#print qr
	#rc = doQuery("1234567890123456124578")
	#print rc
	
	#txt = u"000"
	#gtxt = txt.encode("gbk")
	#utxt = txt.encode("utf8")
	#print gtxt, utxt
	#print type(gtxt)
	#print type(utxt)
	#print base64Encode(gtxt)
	#ciph = u"MDAw"
	#print type(base64Decode(ciph))
	
	#while(True):
	#	x1,y1,x2,y2,x3,y3 = map(int, raw_input().split())
	#	if (x1,y1,x2,y2,x3,y3) == (0,0,0,0,0,0):
	#		break
	#	print 'square = ',square((x1,y1),(x2,y2),(x3,y3))

	#vmcList = [11646,11743,11610,11619,11655,11661,11637,11730,11664,11626,11724,11709,11741,11663,11739,11621,11654,11665,11627,11632,11729,11718,11645]
	#print sort_list(vmcList)
	#ipStr = '0.129.1.0'
	#print isIPAddr(ipStr)
	
	#user='abcs_ub89'
	#print param_verify(user)

	
	#make_QR("https://qr.alipay.com/bax08423nnv1nk7vcpcx6064").show()
	
	
	#import types
	#textList = readFileLines('machineMapTest.txt')
	#onlineList=[]
	#for idx in range(1,len(textList)):
	#	if not textList[idx] == '\n':
	#		print textList[idx].split(':')[1].strip(' ;\n')
	#		onlineList.append(int(textList[idx].split(':')[1].strip(' ;\n')))
	
	#writeFile('machineMapSQL.txt', strSQL)
		
	#print dictSort()

	iStr = 'https://qr.alipay.com/bax09309imkro6zxqtuw4039'
	img = make_QR(iStr)
	img.show()

	#setInfoLogConfig()
	#count = 10000
	#while(count):
	#	Log('info','\nmessage 2')
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
	
	#param = 'o";#'
	#reStr = r'[";#\']'
	#m = re.search(reStr, param)
	#if m:
	#	print True
	#else:
	#	print False

	




