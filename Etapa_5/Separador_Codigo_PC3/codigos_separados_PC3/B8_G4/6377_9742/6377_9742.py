from numpy import *

n = input("N: ").upper().split(",")
x = zeros(4, dtype=int)

for i in n:
	if i=="A":
		x[0]+=1
	elif i=="B":
		x[1]+=1
	elif i=="C":
		x[2]+=1
	elif i=="D":
		x[3]+=1
		
print(x)