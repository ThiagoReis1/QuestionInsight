secao = input("Entre com a secao do produto: ").upper()

i = 0
valor = 0

while i < len(secao):
	if secao[i] == "B":
		valor = valor + 3.75
	elif secao[i] == "C":
		valor = valor + 7.90
	elif secao[i] == "E":
		valor = valor + 9.85
		
	i = i + 1
print(round(valor,2))
		