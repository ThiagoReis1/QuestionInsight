combustivel = int(input("Combustivel comum: "))

if combustivel < 17.5:
	salto = combustivel + 10.5
elif combustivel >= 17.5 and combustivel < 35:
	salto = combustivel + 14
elif combustivel >= 35 and combustivel < 50:
	salto = combustivel + 18.6
elif combustivel >= 50:
	salto = combustivel + 24.5
print(salto)	