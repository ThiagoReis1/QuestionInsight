from numpy import *

m = input("insira os produtos").upper().split(",")
k = 0
v = zeros(4 , dtype = int)
for i in m:
	if i == "A":
		v[0] +=  1
	elif i == "B":
	 	v[1] += 1
	elif i == "L":
		v[2] += 1
	elif i == "H":
		v[3] += 1
	
print(v)