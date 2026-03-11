palavra = input("Insira a palavra desejada: ").upper()
i = 0
total = 0

while i < len(palavra):
	if palavra[i] == "D":
		total += 1
	i += 1
print(total)