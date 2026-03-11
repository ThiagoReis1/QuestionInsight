from numpy import *

x = input("digite: ")
a = -1

for i in len(x):
	x[i] = x[-2]
	
print (x)