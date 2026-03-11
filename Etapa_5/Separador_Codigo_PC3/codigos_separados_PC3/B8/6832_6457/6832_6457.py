s = input("Digite a string: ")

preco = 0
i = 0

while i < len(s):
	if s[i] == "H":
		preco = preco + 5.40
	elif s[i] == "C":
		preco = preco + 8.95
	elif s[i] == "L":
		preco = preco + 4.50
	i = i + 1
print(round(preco, 2))