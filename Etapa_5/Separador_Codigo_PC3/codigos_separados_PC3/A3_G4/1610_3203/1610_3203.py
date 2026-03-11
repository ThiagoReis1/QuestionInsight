from numpy import *

x = str(input()).split(',')

i=0
soma=0

while (i<size(x)):
	if x[i]>0:
		i=i+1
		print(sum(x))