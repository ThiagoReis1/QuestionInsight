s = input("quantas compras? ").upper()

bebidas = 6.80
congelados = 11.75
mercearia = 5.90

i = 0
c = 0

while i < len(s):
	if s[i] == "B":
		c = c + bebidas
	elif s[i] == "C":
		c = c + congelados
	elif s[i] == "M":
		c = c + mercearia
	i = i + 1
print(round(c,2))
		
		