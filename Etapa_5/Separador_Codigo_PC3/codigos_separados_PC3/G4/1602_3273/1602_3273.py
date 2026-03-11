from numpy import *

v = array(eval(input("tempo de chegada:")))
i = 0
while i< size(v):
	if v[i]== max(v):
		print(i)
	i = i + 1

