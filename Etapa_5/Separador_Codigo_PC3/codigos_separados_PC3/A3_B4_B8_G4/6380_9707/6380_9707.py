from numpy import *
v = input().split(',')
n = zeros(4 ,dtype=int)
for i in range(size(n)):
	if n[0] == "E":
		n[i] += 1
	elif n[1] == "V":
		n[i] += 1
	elif n[2] == "A":
		n[i] += 1
	elif n[3] == "D":
		n[i] += 1
print(n)