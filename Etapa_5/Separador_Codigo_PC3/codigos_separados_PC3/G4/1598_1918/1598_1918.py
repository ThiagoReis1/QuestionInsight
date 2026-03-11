from numpy import*
vet =  array(eval(input("")))
k = 0
s = 0.0
while( k < size(vet)):
	if(vet[k] > 80):
		s = s + 0.95*vet[k]
	else:
		s = s + vet[k]
	k = k + 1
print(round(s,2))
		


	