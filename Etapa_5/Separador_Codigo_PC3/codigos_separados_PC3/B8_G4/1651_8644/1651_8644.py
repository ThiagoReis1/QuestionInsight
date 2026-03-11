from numpy import *

s = input("").upper().split(",")
v = zeros(6, dtype = int)

for i in range(len(s)):
	if(s[i] == "MC"):
		v[0] += 1
	elif(s[i] == "C"):
		v[1] += 1
	elif(s[i] == "CM"):
		v[2] += 1
	elif(s[i] == "EM"):
		v[3] += 1
	elif(s[i] == "E"):
		v[4] += 1
	elif(s[i] == "ME"):
		v[5] += 1
print(max(v))
print(v)	
