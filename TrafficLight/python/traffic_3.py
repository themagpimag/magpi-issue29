#!/usr/bin/python

# This program is for the bidirectional traffic light project from Brian Grawburg.
# This for the printed circuit board
# As of this writing (5/2014) only Python 2.7 supports smbus. Trying to run
#    using Python 3 or later will result in an error

import smbus
import sys
import time

# North lights
#   n_green_led		GPA0, pin 28 ||  n_amber_led 	GPA1, pin 27
#   n_red_led		GPA2, pin 26 || 
# East lights
#   e_green_led		GPA3, pin 25 ||  e_amber_led	GPA4, pin 24
#   e_red_led		GPA5, pin 23

bus = smbus.SMBus(1)

address1 	= 0x21		# address of MCP23017
IODIRA_1 	= 0x00 		# Pin direction register, bank A
OLATA_1  	= 0x14		# Register for bank A output latches
GPIOA_1  	= 0x12 		# Register for inputs  
IODIRB_1	= 0x01
OLATB_1		= 0x15
GPIOB_1		= 0x13
address2 	= 0x20
IODIRA_2	= 0x00
OLATA_2		= 0x14
GPIOA_2		= 0x12

light_on = 5
both_red = 1

bus.write_byte_data(address1,IODIRA_1,0x00)	# Set all to outputs
bus.write_byte_data(address1,IODIRB_1,0x00)	# Set all to outputs
bus.write_byte_data(address2,IODIRA_2,0x03)	# Set 1 & 2 as input, others as as output

#Set all bank A, chip 21H as low
bus.write_byte_data(address1,OLATA_1,0x00)		# 0b00000000
#Set all bank B, chip 21H as low
bus.write_byte_data(address1,OLATB_1,0x00)		# 0b00000000

def cycle_1():
	# Straight East Green, North Red, left turns Red
	bus.write_byte_data(address1,OLATA_1,0x30)			#0b00110000
	bus.write_byte_data(address1,OLATB_1,0x24)			#0b00100100
	time.sleep(light_on)
	
def cycle_2():
	# Straight East Amber, North Red
	bus.write_byte_data(address1,OLATA_1,0x28)			#0b00101000
	bus.write_byte_data(address1,OLATB_1,0x24)			#0b00101000
	time.sleep(light_on)
			
def cycle_3():
	# East & North Red, including left turn lanes
	bus.write_byte_data(address1,OLATA_1,0x24)			#0b00100100
	bus.write_byte_data(address1,OLATB_1,0x24)			#0b00100100
	time.sleep(both_red)	

def cycle_4():
	# North Green, East Red
	bus.write_byte_data(address1,OLATA_1,0x84)			#0b10000100
	bus.write_byte_data(address1,OLATB_1,0x24)			#0b00100100
	time.sleep(light_on)	

def cycle_5():
	# North Amber, East Red
	bus.write_byte_data(address1,OLATA_1,0x44)			#0b01000100
	bus.write_byte_data(address1,OLATB_1,0x24)			#0b00100100
	time.sleep(light_on)

def cycle_6():
	# Both left turns Green, straights Red
	bus.write_byte_data(address1,OLATA_1,0x24)			#0b00100100	
	bus.write_byte_data(address1,OLATB_1,0x09)			#0b00001001
	time.sleep(4)

def cycle_7():
	# Both lefts Amber
	bus.write_byte_data(address1,OLATA_1,0x24)			#0b00100100	
	bus.write_byte_data(address1,OLATB_1,0x12)			#0b00010010
	time.sleep(4)

#Set bank A, chip 20 as low to reset NOR gate
bus.write_byte_data(address2,OLATA_2,0x00)		

try:
	while True:
		buttonPressed=bus.read_byte_data(address2,GPIOA_2)
		#print buttonPressed
		if buttonPressed == 0:
			cycle_1()
			cycle_2()
			cycle_3()
			cycle_4()
			cycle_5()
			cycle_3()
		else:
			#print bus.read_byte_data(address2,GPIOA_2)
			cycle_6()
			cycle_7()
			cycle_3()
			#reset the flip-flop
			bus.write_byte_data(address2,OLATA_2,0x04)
			bus.write_byte_data(address2,OLATA_2,0x08)
			bus.write_byte_data(address2,OLATA_2,0x00)
			
			
except KeyboardInterrupt:	
	bus.write_byte_data(address1,OLATA_1,0x00)	
	bus.write_byte_data(address1,OLATB_1,0x00)	
	bus.write_byte_data(address2,OLATA_2,0x00)	
	
			

