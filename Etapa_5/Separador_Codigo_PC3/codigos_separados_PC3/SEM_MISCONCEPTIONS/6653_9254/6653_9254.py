from numpy import*
notas = array(eval(input("insira as notas: ")))

pesos = array([3, 5, 1])
i = 0  #variavel contadora
num = 0


while i < size(notas):
	num = num + (notas[i] * pesos[i])
	i += 1
soma = sum(pesos)
total = num/soma

print(round(total, 2))