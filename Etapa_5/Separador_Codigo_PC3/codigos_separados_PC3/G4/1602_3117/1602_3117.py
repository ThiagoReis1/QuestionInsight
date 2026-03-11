from numpy import *

v = array(eval(input("tempo de chegada: ")))

c = 0

while c < size(v):
	if v[c] == max(v):
		print(c)
	c = c + 1