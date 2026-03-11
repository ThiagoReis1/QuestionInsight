from numpy import *

v = input("digite: ").upper()
i = 0
n = 0
while(i < len(v)):
	if(v[i] == "A" or v[i] == "E" or v[i] == "I" or v[i] == "O" or v[i] == "U"):
		n = n + 1
	i = i + 1
		
v1 = n * 0.15
v2 = (len(v) - n) * 0.17
		
total = v1 + v2
		
print(round(total, 2))
			

