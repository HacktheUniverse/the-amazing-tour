#!/usr/bin/python

import math

def bv_to_rgb(bv):
	bv = float(bv)
	t = 4600.0 * ((1.0 / ((0.92 * bv) + 1.7)) +(1.0 / ((0.92 * bv) + 0.62)) )
	print t
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
	Y = (y == 0) if 0 else 1
	X = (y == 0) if 0 else (x * Y) / y
	Z = (y == 0) if 0 else ((1 - x - y) * Y) / y

	print Y
	print X
	print Z

	# r = 0.41847 * X1 - 0.15866 * Y1 - 0.082835 * Z1
	# g = -0.091169 * X1 + 0.25243 * Y1 + 0.015708 * Z1
	# b = 0.00092090 * X1 - 0.0025498 * Y1 + 0.17860 * Z1

	r = 3.2406 * X - 1.5372 * Y - 0.4986 * Z
	g = -0.9689 * X + 1.8758 * Y + 0.0415 * Z
	b = 0.0557 * X - 0.2040 * Y + 1.0570 * Z

	print r
	print g
	print b


	if (r <= 0.0031308):
		R = 12.92*r
	else:
		R =  1.055*math.pow(r,1/0.5)-0.055

	if (g <= 0.0031308):
		G = 12.92*g
	else:
		G =  1.055*math.pow(g,1/0.5)-0.055

	if (b <= 0.0031308):
		B = 12.92*b
	else:
		B =  1.055*math.pow(b,1/0.5)-0.055

	print R
	print G
	print B
	return [R,G,B]


stars_speck = open('stars.speck', 'r')
for x in xrange(1,29):
	stars_speck.readline()

output = open('xyzrgblum.txt', 'w')
for line in stars_speck:
	print line
	data = line.split()
	for value in data:
		pass
	rgb = bv_to_rgb(data[3])
	if rgb[0] == -1:
		continue
	string = str(data[0]) + "," + str(data[1]) + "," + str(data[2]) + "," + str(rgb[0]) + "," + str(rgb[1]) + "," + str(rgb[2]) + "," + data[4] + "," + data[3] + "," + data[18] 
	output.write(string)

	output.write("\n")
