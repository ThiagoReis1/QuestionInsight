from numpy import *
a = array(eval(input("insira o vetor: ")))
j = 0
for i in range(size(a)):
	j = j + a[i]
	if(a[i] == 0):
		j = 0
		j = j + a[i]
print(j)