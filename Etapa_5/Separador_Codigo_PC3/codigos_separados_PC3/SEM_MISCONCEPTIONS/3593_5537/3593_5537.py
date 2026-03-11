from numpy import*
vet = array(eval(input("Digite: ")))
i = 0
pontos = 200
while(i < size(vet)):
	if((vet[i] % 2)  == 0):
		pontos = pontos * 3
	else:
		pontos = pontos / 2
	i = i + 1
print(round(pontos,2))
		