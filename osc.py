#!/usr/bin/python

import OSC

c = OSC.OSCClient()
c.connect(('10.20.12.197',57120))

stars_speck = open('stars.speck', 'r')
for x in xrange(1,29):
	stars_speck.readline()

# output = open('xyzrgblum.txt', 'w')
for line in stars_speck:
	print line
	data = line.split()
	oscmsg = OSC.OSCMessage()
	oscmsg.setAddress("/startup")
	oscmsg.append(str(data[3]))
	c.send(oscmsg)


	# rgb = bv_to_rgb(data[3])
	# if rgb[0] == -1:
	# 	continue
	# string = str(data[0]) + "," + str(data[1]) + "," + str(data[2]) + "," + str(rgb[0]) + "," + str(rgb[1]) + "," + str(rgb[2]) + "," + data[4] + "," + data[3] + "," + data[18] 
	# output.write(string)

	# output.write("\n")
