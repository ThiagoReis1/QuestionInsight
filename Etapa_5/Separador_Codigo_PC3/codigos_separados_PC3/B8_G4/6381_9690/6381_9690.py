from numpy import *

s = input("cartas: ").upper().split(",")
v = zeros(4,dtype=int)

for i in range(len(s)):
	if s[i]=="C":
		v[0]+=1
	elif s[i]=="O":
		v[1]+=1
	elif s[i]=="P":
		v[2]+=1
	elif s[i]=="E":
		v[3]+=1
print(v)