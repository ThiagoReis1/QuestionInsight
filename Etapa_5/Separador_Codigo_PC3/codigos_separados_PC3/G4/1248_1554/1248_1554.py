from numpy import *

v=array[(float(input()))]
x=array[x1,x2]

C = 0.75 * A + 0.25 * B
D = 0.25 * A + 0.75 * B

for x in v:
	if (C <= size(v) and size(v) < D):
		x1= size(v)
	elif (D <= size(v) and size(v) < B):
		x2= size(v)
	else:
		print(x)