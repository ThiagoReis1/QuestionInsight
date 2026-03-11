from numpy import*
vet = array(eval(input("")))
soma = (sum(vet))
i = 0
d= 0
while(i<size(vet)):
	if(vet[i]>80):
		d=d+1
	i=i+1
c= soma-(15/100)*d
print(round(c,2))