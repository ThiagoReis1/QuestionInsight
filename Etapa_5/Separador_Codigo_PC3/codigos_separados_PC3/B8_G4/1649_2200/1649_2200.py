from numpy import *
s = input().split(',')
n = zeros(5, dtype=int)
for i in s:
	if(i == "P"):
		n[0] = n[0] + 1
	elif(i == "C"):
		n[1] = n[1] + 1
	elif(i == "M"):
		n[2] = n[2] + 1
	elif(i == "V"):	
		n[3] = n[3] + 1
	elif(i == "A"):
		n[4] = n[4] + 1
print(max(n))
print(n)