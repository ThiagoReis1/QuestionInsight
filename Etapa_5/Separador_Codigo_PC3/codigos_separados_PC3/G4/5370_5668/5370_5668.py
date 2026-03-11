from numpy import *
v = array(eval(input("vetor: ")))
i = 0

while i < v[-2]:
	if v[i+1] >= v[i]:
		m = "True"
	else:
		m = "False"
	i+=1

print(m)