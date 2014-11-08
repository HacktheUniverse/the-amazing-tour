#!/usr/bin/python

import math
from visual import *
# from visual import display
import time

def bv_to_rgb(bv):
	bv = float(bv)
	t = 4600.0 * ((1.0 / ((0.92 * bv) + 1.7)) +(1.0 / ((0.92 * bv) + 0.62)) )
	rcode = 0

	if t>=1667 and t<=4000:
		x = ((-0.2661239 * math.pow(10,9)) / math.pow(t,3)) + ((-0.2343580 * math.pow(10,6)) / math.pow(t,2)) + ((0.8776956 * math.pow(10,3)) / t) + 0.179910
	elif t > 4000 and t <= 25000 :
		x = ((-3.0258469 * math.pow(10,9)) / math.pow(t,3)) + ((2.1070379 * math.pow(10,6)) / math.pow(t,2)) + ((0.2226347 * math.pow(10,3)) / t) + 0.240390
	else:
		rcode = -1


	if (t >= 1667 and t <= 2222):
		y = -1.1063814 * math.pow(x,3) - 1.34811020 * math.pow(x,2) + 2.18555832 * x - 0.20219683
	elif (t > 2222 and t <= 4000):
		y = -0.9549476 * math.pow(x,3) - 1.37418593 * math.pow(x,2) + 2.09137015 * x - 0.16748867
	elif (t > 4000 and t <= 25000):
		y = 3.0817580 * math.pow(x,3) - 5.87338670 * math.pow(x,2) + 3.75112997 * x - 0.37001483
	else:
		rcode = -1

	if rcode == -1:
		return [-1]

	# xyY to XYZ, Y = 1
	Y = 0 if (y == 0) else 1
	X = 0 if (y == 0) else (x * Y) / y
	Z = 0 if (y == 0) else ((1 - x - y) * Y) / y

	r = 3.2406 * X - 1.5372 * Y - 0.4986 * Z
	g = -0.9689 * X + 1.8758 * Y + 0.0415 * Z
	b = 0.0557 * X - 0.2040 * Y + 1.0570 * Z

	R = 12.92*r if (r <= 0.0031308) else 1.055*math.pow(r,1/0.5)-0.055
	G = 12.92*g if (g <= 0.0031308) else 1.055*math.pow(g,1/0.5)-0.055
	B = 12.92*b if (b <= 0.0031308) else 1.055*math.pow(b,1/0.5)-0.055

	return [R,G,B]

# scene = display()
# scene.stereo='crosseyed'
# scene.stereodepth = 2
# scene.scale = (10,10,10)
# pointerx = arrow(pos=(0,0,0), axis=(500,0,0), shaftwidth=1)
# pointerx.color = (255,0,0)
# pointery = arrow(pos=(0,0,0), axis=(0,500,0), shaftwidth=1)
# pointery.color = (0,255,0)
# pointerz = arrow(pos=(0,0,0), axis=(0,0,500), shaftwidth=1)
# pointerz.color = (0,0,255)
stars_speck = open('stars.speck', 'r')
for x in xrange(1,29):
	stars_speck.readline()

output = open('xyzrgblum.txt', 'w')
number_of_stars=3500
for i in range(1,number_of_stars):
	line = stars_speck.readline()
	data = line.split()
	rgb = bv_to_rgb(data[3])
	if rgb[0] == -1:
		continue
	if float(data[4]) > 100.0 or i == 1:
		# print str(data[4]) + " MAKING SPHERE!"
		newsphere = sphere()
		newsphere.pos = (float(data[0]), float(data[1]), float(data[2]))
		newsphere.color = rgb
		# newsphere.opacity = 0.5
		absolute_mag = float(data[5])
		newsphere.radius = math.log(float(data[4]))/1.5
	else:
		# print str(data[4]) + " NOT MAKING SPHERE!"
		newsphere = points()
		newsphere.pos = (float(data[0]), float(data[1]), float(data[2]))
		newsphere.color = rgb
		# newsphere.opacity = 0.5
		absolute_mag = float(data[5])
		newsphere.size = math.log(float(data[4]))

	string = str(data[0]) + "," + str(data[1]) + "," + str(data[2]) + "," + str(rgb[0]) + "," + str(rgb[1]) + "," + str(rgb[2]) + "," + data[4] + "," + data[3] + "," + data[18] 
	output.write(string)

	output.write("\n")
	#skip a bunch of lines to get a more evenly spaced data set
	for x in xrange(1,100000/number_of_stars):
		stars_speck.readline()

scene.forward = (1,1,0)

# while 1:
# 	scene.forward = scene.forward.rotate(math.pi/180)
# 	time.sleep(.2)
