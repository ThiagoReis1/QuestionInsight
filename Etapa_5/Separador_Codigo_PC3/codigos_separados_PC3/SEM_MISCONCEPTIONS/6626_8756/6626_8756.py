palavra = input("").upper()
i = 0
cont = 0

while i < len(palavra):
	if palavra[i] == "C":
		cont = cont + 1
	i = i + 1
print(cont)