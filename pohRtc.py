#!/usr/bin/python3
# -*- coding: utf-8 -*-
from smbus2 import SMBus
import time

#sec min hour week day mout year
#NowTime = [0x00,0x00,0x18,0x04,0x12,0x08,0x15]
#w  = ["SUN","Mon","Tues","Wed","Thur","Fri","Sat"]
#address=0x68, register=0x00
#bus = SMBus(1) #/dev/i2c-1

w  = ["SUN","Mon","Tues","Wed","Thur","Fri","Sat"]

class RTC():
	def __init__(self, busNumber=1, address=0x68, registro=0x00, module="ds3231"):
		self.address = address
		self.register = registro
		self.bus = SMBus(busNumber)
		self.device = module
	
	def SetTime(self, NowTime):
		self.bus.write_i2c_block_data(self.address,self.register,NowTime)
		
	def ReadTime(self):
		return self.bus.read_i2c_block_data(self.address,self.register,7)

	def Date(self):
		t = self.ReadTime()
		print(t)
		month = t[5]&0x1F
		day = t[4]&0x3F
		year = t[6]
		print("20%x/%02x/%02x" % (year,month,day))

	def Ticks(self):
		print("")


	def Now(self):
		
		t = self.ReadTime()
		t[0] = t[0]&0x7F  #sec
		t[1] = t[1]&0x7F  #min
		t[2] = t[2]&0x3F  #hour
		t[3] = t[3]&0x07  #week
		t[4] = t[4]&0x3F  #day
		t[5] = t[5]&0x1F  #mouth
		print("20%x/%02x/%02x %02x:%02x:%02x %s" %(t[6],t[5],t[4],t[2],t[1],t[0],w[t[3]-1]))