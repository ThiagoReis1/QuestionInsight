from numpy import*
notas = array(eval(input("notas: ")))
pesos = ([5,1])
i = 0
c = 0
while i < size(notas):
	np = notas[i] * pesos[i]
	c += np
	i += 1
total = c/6
print(round(total, 2))