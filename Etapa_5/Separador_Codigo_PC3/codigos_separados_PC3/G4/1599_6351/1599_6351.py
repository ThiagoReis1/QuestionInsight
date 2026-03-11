from numpy import*

vet = array(eval(input("valor da compra: ")))
s = 0
i = 0

while(i<size(vet)):
	if(vet[i]>80.00):
		s = s + vet[i]-(vet[i]*(15/100))
	else:
		s = s + vet[i]
	i = i + 1
print(round(s,2))