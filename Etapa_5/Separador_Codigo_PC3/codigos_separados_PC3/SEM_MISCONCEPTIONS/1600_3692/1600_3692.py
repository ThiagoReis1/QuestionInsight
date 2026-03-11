from numpy import*
vet = array(eval(input()))
x=0
while x < size(vet):
	if vet[x] > 80:
		vet[x]= vet[x]-(vet[x]*0.15)
	x=x+1
	
total = sum(vet)
print(round(total,2))