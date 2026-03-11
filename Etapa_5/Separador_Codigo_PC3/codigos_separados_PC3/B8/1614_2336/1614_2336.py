from numpy import*
alimento = array(eval(input()))
quantidades = array(eval(input()))

i = 0
cont=0
while i < size(alimento):
	if alimento[i] == "BANANA":
		cont += 0.97 * quantidades[i]
	elif alimento[i] == "BIFE":
		cont += 2.95 * quantidades[i]
	elif alimento[i] == "FEIJOADA":
		cont += 1.27 * quantidades[i]
	elif alimento[i] == "OMELETE":
		cont += 1.04 * quantidades[i]
	elif alimento[i] == "TOMATE":
		cont += 0.2 * quantidades[i]
	i= i+1
print(cont)
	