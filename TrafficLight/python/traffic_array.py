#!/usr/bin/python

import smbus
import time

bus = smbus.SMBus(1)

address1 	= 0x21
address2 	= 0x20
IODIRA	 	= 0x00
IODIRB		= 0x01
GPIOA  		= 0x12
GPIOB		= 0x13
OLATA  		= 0x14
OLATB		= 0x15

io_setting = [
		[0,0,0],	# Reset: all off, no delay
		[0x30,0x24,5],	# Straight East Green, North Red, L-turns Red
		[0x28,0x24,5],	# Straight East Amber, North Red
		[0x24,0x24,1],	# East & North Red, L-turns Red
		[0x84,0x24,5],	# North Green, East Red
		[0x44,0x24,5],	# North Amber, East Red
		[0x24,0x09,4],	# Both L-turns Green, Straights Red
		[0x24,0x12,4]	# Both L-turns Amber
	     ]

def cycle(index):
	bus.write_byte_data(address1,OLATA,io_setting[index][0])
	bus.write_byte_data(address1,OLATB,io_setting[index][1])
	time.sleep(io_setting[index][2])

bus.write_byte_data(address1,IODIRA,0x00)
bus.write_byte_data(address1,IODIRB,0x00)
bus.write_byte_data(address2,IODIRA,0x03)

cycle(0)

bus.write_byte_data(address2,OLATA,0x00)		

try:
	while True:
		buttonPressed=bus.read_byte_data(address2,GPIOA)
		if buttonPressed == 0:
			cycle(1)
			cycle(2)
			cycle(3)
			cycle(4)
			cycle(5)
			cycle(3)
		else:
			cycle(6)
			cycle(7)
			cycle(3)
			bus.write_byte_data(address2,OLATA,0x04)
			bus.write_byte_data(address2,OLATA,0x08)
			bus.write_byte_data(address2,OLATA,0x00)
			
except KeyboardInterrupt:
	cycle(0)
