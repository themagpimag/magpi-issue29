#!/usr/bin/env python
import os
dev_dir = '/sys/bus/w1/devices/'
devices = os.listdir(dev_dir) 
devices.remove('w1_bus_master1') 
for dev in devices: 
  f = open(dev_dir + dev + '/w1_slave', 'r') 
  content = f.readlines() 
  temp_start = content[1].find('t=') 
  print content[1][temp_start + 2:] + dev 
  f.close()
