from numpy import*

vet = array(eval(input("Digite o valor de vetores: ")))
total = 0

for i in vet:
	total = total + i
	if total >= 55:
		total = 0
print(total)