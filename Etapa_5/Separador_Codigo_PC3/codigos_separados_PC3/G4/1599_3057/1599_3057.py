from numpy import*
vet = array(eval(input("Informe os custos dos intens: ")))
#i = 0
soma = 0
x = 0
#while (i< size(vet)):
for i in range (size(vet)):
	if (vet[i]> 80.0):
		soma = soma + (vet[i] - (vet[i] * 0.15))
		i +1
	else:
		x = x + vet[i]
a = soma + x
print(round(a,2))