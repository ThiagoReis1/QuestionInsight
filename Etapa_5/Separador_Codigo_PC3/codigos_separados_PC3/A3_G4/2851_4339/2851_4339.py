from numpy import*
v1= array(eval(input("valor do vetor:")))
soma=0

for x in range(size(v1)):
	if v1[x] == 99:
		soma= v1[x] 
	else:
		v1[x]= v1[x]
print(sum(v1))