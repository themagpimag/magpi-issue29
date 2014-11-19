#!/usr/bin/python

import smbus
import sys
import time

bus = smbus.SMBus(1)

address1 	= 0x21
address2 	= 0x20
IODIRA	 	= 0x00
OLATA  		= 0x14
GPIOA  		= 0x12
IODIRB		= 0x01
OLATB		= 0x15
GPIOB		= 0x13

light_on = 5
both_red = 1

bus.write_byte_data(address1,IODIRA,0x00)
bus.write_byte_data(address1,IODIRB,0x00)
bus.write_byte_data(address2,IODIRA,0x03)
bus.write_byte_data(address1,OLATA,0x00)
bus.write_byte_data(address1,OLATB,0x00)

def cycle_1():
	bus.write_byte_data(address1,OLATA,0x30)
	bus.write_byte_data(address1,OLATB,0x24)
	time.sleep(light_on)
	
def cycle_2():
	bus.write_byte_data(address1,OLATA,0x28)
	bus.write_byte_data(address1,OLATB,0x24)
	time.sleep(light_on)
			
def cycle_3():
	bus.write_byte_data(address1,OLATA,0x24)
	bus.write_byte_data(address1,OLATB,0x24)
	time.sleep(both_red)	

def cycle_4():
	bus.write_byte_data(address1,OLATA,0x84)
	bus.write_byte_data(address1,OLATB,0x24)
	time.sleep(light_on)	

def cycle_5():
	bus.write_byte_data(address1,OLATA,0x44)
	bus.write_byte_data(address1,OLATB,0x24)
	time.sleep(light_on)

def cycle_6():
	bus.write_byte_data(address1,OLATA,0x24)
	bus.write_byte_data(address1,OLATB,0x09)
	time.sleep(4)

def cycle_7():
	bus.write_byte_data(address1,OLATA,0x24)
	bus.write_byte_data(address1,OLATB,0x12)
	time.sleep(4)

bus.write_byte_data(address2,OLATA,0x00)		

try:
	while True:
		buttonPressed=bus.read_byte_data(address2,GPIOA)
		if buttonPressed == 0:
			cycle_1()
			cycle_2()
			cycle_3()
			cycle_4()
			cycle_5()
			cycle_3()
		else:
			cycle_6()
			cycle_7()
			cycle_3()
			bus.write_byte_data(address2,OLATA,0x04)
			bus.write_byte_data(address2,OLATA,0x08)
			bus.write_byte_data(address2,OLATA,0x00)
			
			
except KeyboardInterrupt:	
	bus.write_byte_data(address1,OLATA,0x00)	
	bus.write_byte_data(address1,OLATB,0x00)	
	bus.write_byte_data(address2,OLATA,0x00)	

