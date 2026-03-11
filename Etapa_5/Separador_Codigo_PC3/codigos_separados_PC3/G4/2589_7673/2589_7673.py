from numpy import * 

vet = array(eval(input()))

a = 0
i = 1
while(i<size(vet)):
	if(vet[0] <= vet[i]):
		print(i)
		a=a+1
	i = i + 1
print(a)