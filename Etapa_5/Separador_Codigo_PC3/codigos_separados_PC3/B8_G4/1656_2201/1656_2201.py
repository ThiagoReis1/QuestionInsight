from numpy import *
a = input().split(',')
n = zeros(5, dtype=int)
for i in a:	
	if(i == "BE"):
		n[0] = n [0] + 1
	elif(i == "ES"):
		n[1] = n [1] + 1
	elif(i == "FR"):
		n[2] = n [2] + 1
	elif(i == "IT"):
		n[3] = n [3] + 1
	elif(i == "PT"):
		n[4] = n [4] + 1
print(max(n))
print(n)