from numpy import *
s = array(eval(input("")))
n = zeros(4,dtype=int)
for i in s:
	if(i == "BOTAFOGO"):
		n[0] = n[0] + 1
	elif(i == "FLAMENGO"):
		n[1] = n[1] + 1
	elif(i == "FLUMINENSE"):
		n[2] = n[2] + 1
	elif(i == "VASCO"):	
		n[3] = n[3] + 1
print(n)			 