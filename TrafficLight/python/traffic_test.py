#!/usr/bin/python
# This program is for the bidirectional traffic light project from Brian Grawburg.
# As of this writing (8/2014) only Python 2.7 supports smbus. Trying to run using 
# Python 3 or later will result in an error
import smbus
import sys
import os
import time

bus = smbus.SMBus(1)

address1 = 0x21 # address of MCP23017
IODIRA_1 = 0x00 # Pin direction register, bank A
OLATA_1 = 0x14 # Register for bank A output latches
GPIOA_1 = 0x12 # Register for inputs
IODIRB_1 = 0x01
OLATB_1 = 0x15
GPIOB_1 = 0x13

bus.write_byte_data(address1,IODIRA_1,0x00) # Set all to outputs
bus.write_byte_data(address1,IODIRB_1,0x00)

#Set all bank A & B pins low
bus.write_byte_data(address1,OLATA_1,0x00) # 0b00000000
bus.write_byte_data(address1,OLATB_1,0x00)

# WHB comment : DO NOT NEED A WHILE LOOP.

while True:
#test all lights
  bus.write_byte_data(address1,OLATA_1,0x80) #0b10000000
  print "North green: ", bus.read_byte_data(address1,GPIOA_1)
  time.sleep(.5)

  bus.write_byte_data(address1,OLATA_1,0x40) #0b01000000
  print "North amber: ",bus.read_byte_data(address1,GPIOA_1)
  time.sleep(.5)

  bus.write_byte_data(address1,OLATA_1,0x20) #0b00100000
  print "North red: ",bus.read_byte_data(address1,GPIOA_1)
  time.sleep(.5)

  bus.write_byte_data(address1,OLATA_1,0x10) #0b00010000
  print "East green: ",bus.read_byte_data(address1,GPIOA_1)
  time.sleep(.5)

  bus.write_byte_data(address1,OLATA_1,0x8) #0b00001000
  print "East amber: ",bus.read_byte_data(address1,GPIOA_1)
  time.sleep(.5)

  bus.write_byte_data(address1,OLATA_1,0x4) #0b00000100
  print "East red: ",bus.read_byte_data(address1,GPIOA_1)
  time.sleep(.5)

  bus.write_byte_data(address1,OLATB_1,0x1)
  print "North Left red: ",bus.read_byte_data(address1,GPIOB_1)
  time.sleep(.5)

  bus.write_byte_data(address1,OLATB_1,0x02)
  print "North Left amber: ",bus.read_byte_data(address1,GPIOB_1)
  time.sleep(.5)

  bus.write_byte_data(address1,OLATB_1,0x04)
  print "North Left red: ",bus.read_byte_data(address1,GPIOB_1)
  time.sleep(.5)

  bus.write_byte_data(address1,OLATB_1,0x8)
  print "East Left green: ",bus.read_byte_data(address1,GPIOB_1)
  time.sleep(.5)

  bus.write_byte_data(address1,OLATB_1,0x10)
  print "East Left amber: ",bus.read_byte_data(address1,GPIOB_1)
  time.sleep(.5)

  bus.write_byte_data(address1,OLATB_1,0x20)
  print "East Left red: ",bus.read_byte_data(address1,GPIOB_1)
  time.sleep(.5)

#stop process
  bus.write_byte_data(address1,OLATA_1,0x00) #0b00000000
  bus.write_byte_data(address1,OLATB_1,0x00)
  print "End:"
  sys.exit()
