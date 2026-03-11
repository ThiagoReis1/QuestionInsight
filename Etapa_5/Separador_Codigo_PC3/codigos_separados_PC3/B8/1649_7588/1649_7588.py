from numpy import *

s = input().split(',')

vCont = zeros(5, dtype = int)

for i in range(len(s)):
	if(s[i] == 'P'):
		vCont[0] += 1
	elif(s[i] == 'C'):
		vCont[1] += 1
	elif(s[i] == 'M'):
		vCont[2] += 1
	elif(s[i] == 'V'):
		vCont[3] += 1
	elif(s[i] == 'A'):
		vCont[4] += 1

print(max(vCont))
print(vCont)