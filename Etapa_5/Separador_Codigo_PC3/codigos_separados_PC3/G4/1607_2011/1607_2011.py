from numpy import * 
vet = array(eval(input(" ")))
soma=0
i=0
x=0
while(i<size(vet)-1):
	soma = soma + abs(vet[i]-vet[-size(vet)+x+1])
	i=i+1
	x=x+1
print(soma*3)