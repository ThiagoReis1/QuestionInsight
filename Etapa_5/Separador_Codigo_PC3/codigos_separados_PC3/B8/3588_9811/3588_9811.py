from numpy import *

rings = array(eval(input("qual posicao:")))

i = 0
points = 10000

while i < size(rings):
	if rings[i] == 1:
		points *= 2
	elif rings[i] == 3:
		points /= 2
	elif rings[i] == 4:
		points /= 4
	i += 1
	
print(round(points, 2))