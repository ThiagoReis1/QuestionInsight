moeda = input("moeda: ").upper()
faces = moeda
soma = 0
i = 0

while moeda != "S":
	if moeda == "CARA":
		soma = soma + 1
		i = i + 1 
	elif moeda == "COROA":
		soma = soma + 1
	moeda = input("moeda: ").upper()
	
pct = (i * 100) / soma
print(soma)
print(round(pct, 2))


