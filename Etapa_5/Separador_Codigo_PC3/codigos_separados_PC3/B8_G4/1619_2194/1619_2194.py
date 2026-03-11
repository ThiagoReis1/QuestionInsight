from numpy import *
n = array(eval(input()))
b = array(eval(input().upper()))
j = 0
dt = 0
while(j < size(n)):
	if(b[j] == "QUENTE"):
		dt = dt + n[j] * 90
	elif(b[j] == "MORNO"):
		dt = dt + n[j] * 45
	elif(b[j] == "FRIO"):
		dt = dt + n[j] * 0
	j = j + 1
dt = dt * 0.005
print(round(dt,2))