from numpy import *
v1 = array(eval(input("v1: ")))
v2 = array(eval(input("v2: ")))
i = 0
while(i < size(v1) and i < size(v2)):
	if(v1[i] == "BIFE"):
		v1[i] = 2.95
		i = i + 1
	elif(v1[i] == "OMELETE"):
		v1[i] = 1.04
		i = i + 1
	elif(v1[i] == "TOMATE"):
		v1[i] = 0.2 
		i = i + 1
print(v1[0] * v2[0] + v1[1] * v2[1] + v1[2] * v2[2])