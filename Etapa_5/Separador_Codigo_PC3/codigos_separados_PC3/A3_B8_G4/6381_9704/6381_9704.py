from numpy import *

b = input().upper().split(',')
a = zeros(4,dtype=int)
cont = 0	

for i in range(size(b)):
	if b[i] == "C":
		a[0]+=1
	elif b[i] == "O":
		a[1]+=1
	elif b[i] == "P":
		a[2]+=1
	elif b[i] == "E":
		a[3]+=1
print(a)