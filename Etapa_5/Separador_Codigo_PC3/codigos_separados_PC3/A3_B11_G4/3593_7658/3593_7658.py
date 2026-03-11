from numpy import *
D= array(eval(input(":")))
p= 200
i= 0
while i < size(D):
	if D[i]==1:
		v= p/2
	if D[i]== 2:
		v= p*3
	if D[i]== 3:
		v= p/2
	if D[i]== 4:
		v= p*3
	if D[i]== 5:
		v= p/2
	if D[i]==6:
		v= p*3
	i= i+1
	p= v
print(round(p,2))