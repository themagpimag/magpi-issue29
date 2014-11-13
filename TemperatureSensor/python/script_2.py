#! /usr/bin/python2.7
import os, time, sys
dev_dir = '/sys/bus/w1/devices/'

def load_modules():
    first_time = 0
    if os.getuid() == 0:   # Only root can load the mods
        if os.system("modprobe --first-time -q w1-gpio") == 0:
            first_time = 1
        if os.system("modprobe --first-time -q w1-therm") == 0:
            first_time = 1
        if first_time:    # wait a bit for the devs to be populated 
            time.sleep(5)
        return first_time
    else:
        if os.system("modprobe -q w1_gpio") == 256 or\
        os.system("modprobe -q w1_therm") == 256:
            print "sorry, modules not loaded and we are not root"
            sys.exit(1)


def read_temp_lines(dev):
    # Note that the read process is slow, bit less than
    # a second per device
    try:
        f = open(dev_dir + dev + '/w1_slave', 'r')
        content = f.readlines()
        f.close()
    except IOError:
        lines = ["no file"]
        return content

def read_temps():
    # Build a tuple with data from each device we know 
    # about, set the ones that are not present to 0.0 
    results = []
    for dev in devices:
        content = read_temp_lines(dev)
        if content == ["no file"]:
            results.append(0.0)
            continue
        while content[0].find("YES") == -1:
            # try again if dev was not ready 
            time.sleep(0.1)
            content = read_temp_lines(dev)
        temp_start = content[1].find('t=')
        if temp_start != -1:
            temp_string = content[1][temp_start+2:]
            results.append(float(temp_string) / 1000.0)
    return results

load_modules()
devices = os.listdir(dev_dir)
devices.remove('w1_bus_master1')
print read_temps()

