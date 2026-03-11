from numpy import*

pr = array(input("Insira os produtos: ").upper())
qt = array(eval(input("Quantidade de produtos: ")))

i = 0

while (i < size(pr)):
	if (pr[i] == "ARROZ"):
		ar = 1.25*qt[i]
	elif (pr[i] == "FEIJAO"):
		fe = 2.60*qt[i]
	elif (pr[i] == "BIS"):
		bi = 1.80*qt[i]
	elif (pr[i] == "MIOJO"):
		mi = 0.85*qt[i]
	elif (pr[i] == "FANTA"):
		fa = 3.20*qt[i]
	i = i + 1

soma = ar + fe + bi + mi + fa
print(round(soma,2))