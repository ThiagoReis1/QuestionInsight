from numpy import*

vet = array(eval(input("digite o vetor: ")))

desc = 6,50

if(vet > 90):
	vet = vet - desc
	valor = sum(vet)
print(round(valor,2))


