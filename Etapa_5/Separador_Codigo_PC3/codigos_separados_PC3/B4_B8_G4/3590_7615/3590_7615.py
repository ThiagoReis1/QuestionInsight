from numpy import *
v= array(eval(input("digite um vetor: ")))
v1= 0
i= 0
while i < size(v):
	if v[i] == 1:
		v1= v1 + 10
	elif v[i] == 2:
		v1= v1 + 5
	elif v[i] == 3:
		v1= v1 + 0
	elif v[i] == 4:
		v1= v1 + 5
	elif v[i] == 5:
		v1= v1 + 20
	elif v[i] == 6:
		v1= v1 +10
	i+=1

print(v1)