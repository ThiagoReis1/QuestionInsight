from numpy import *
vet = array(eval(input("Informe o custo dos items: ")))
i=0
total=0
desc=0.08
menos=0

while i<size(vet):
	if vet[i]>50:
		total=total+(vet[i]-(vet[i]*desc))
		i=i+1
	else:
		total=total+vet[i]
		i=i+1
		
print(round(total, 2))