from numpy import*
vet=array(eval(input("Notas: ")))

i=0

while i<size(vet):
	if vet[i]>8:
		vet[i]=10
	elif vet[i]<2:
		vet[i]=0
	else:
		vet[i]=vet[i]
	i=i+1
print(vet)