from numpy import*

vet = array(eval(input("Digite os valores: ")))

i = 0
acum = 0

while i < size(vet):
	if vet[i] > 80:
		acum = acum + vet[i]*0.85
	else:
		acum = acum + vet[i]
	i = i + 1
print(round(acum,2))
	