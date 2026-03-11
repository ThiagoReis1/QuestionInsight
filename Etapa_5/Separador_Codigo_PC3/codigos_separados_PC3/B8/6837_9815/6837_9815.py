s = input("Insira a Classificacao dos Produtos: ").upper()

i = 0
total = 0
while i < len(s):
	if s[i] == "I":
		total += 3.75
	elif s[i] == "M":
		total += 4.50
	elif s[i] == "S":
		total += 2.90
	i += 1
	
print(round(total, 2))