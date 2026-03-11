from numpy import *

a = input("insira: ").upper().split(",")
b = zeros(4, dtype=int)


for i in range(len(a)):
	if (a[i]) == "A":
		b[0] += 1
	elif (a[i]) == "B":
		b[1] +=1
	elif (a[i]) == "C":
		b[2] += 1
	elif (a[i]) == "D":
		b[3] += 1
print(b)