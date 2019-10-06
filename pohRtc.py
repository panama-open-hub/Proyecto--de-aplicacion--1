#!/usr/bin/python3
# -*- coding: utf-8 -*-
from smbus2 import SMBus
import time
import logging

w  = ["Domingo","Lunes","Martes","Miercoles","Jueves","Viernes","Sabado"] #index 1 to 7
# Lookup table for names of days (nicer printing).
days = ("Domingo","Lunes","Martes","Miercoles","Jueves","Viernes","Sabado")

class RTC():
	def __init__(self, busNumber=1, address=0x68, registro=0x00, module="ds3231"):
		self.address = address
		self.register = registro
		self.bus = SMBus(busNumber)
		self.device = module
	
	def SetTime(self):
		#DS3231 seconds, minutes, hours, day, date, month, year
		NowTime = [0x00,0x00,0x16,0x07,0x5,0x10,0x19]
		self.bus.write_i2c_block_data(self.address,self.register,NowTime)
		
	def ReadTime(self):
		return self.bus.read_i2c_block_data(self.address,self.register,7)

	def Date(self):
		t = self.ReadTime()
		print(t)
		month = t[5]&0x1F
		day = t[4]&0x3F
		year = t[6]
		logging.debug("20%x/%02x/%02x" % (year,month,day))

	def Ticks(self):
		logging.debug("")


	def Hora(self):
		t = self.ReadTime()
		print(t)
		secs = t[0]&0x7F  #sec
		mins = t[1]&0x7F  #min
		hrs = t[2]&0x3F  #hour
		texto = " %02x:%02x:%02x" % (hrs,mins,secs)
		logging.debug(texto)
		return texto

	def Now(self):
		t = self.ReadTime()
		t[0] = t[0]&0x7F  #sec
		t[1] = t[1]&0x7F  #min
		t[2] = t[2]&0x3F  #hour
		t[3] = t[3]&0x07  #week
		t[4] = t[4]&0x3F  #day
		t[5] = t[5]&0x1F  #mouth
		texto = "20%x/%02x/%02x %02x:%02x:%02x %s" %(t[6],t[5],t[4],t[2],t[1],t[0],w[t[3]-1])
		logging.debug(texto)
		return texto

	# Convert normal decimal numbers to binary coded decimal
	def decToBcd(self, val):
		return( (val/10*16) + (val%10) )
	
	#Convert binary coded decimal to normal decimal numbers
	def bcdToDec(self, val):
		return ((val/16*10) + (val%16))
