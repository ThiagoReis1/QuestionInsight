from numpy import*

vet=array(eval(input("custo total da compra: ")))

i = 0
t = 0

while(i<size(vet)):
	if(vet[i]>200):
		t = t - vet[i]*15/100 + vet[i]
	else:
		t = t + vet[i]
		
	i = i + 1

print(round(t, 2))