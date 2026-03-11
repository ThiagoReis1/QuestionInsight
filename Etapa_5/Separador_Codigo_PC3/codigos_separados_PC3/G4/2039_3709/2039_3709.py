n = input()
soma = 0
while (n.upper() != "S"):
	if (n.upper() == "A"):
		soma = soma + 1
		n = input("1° nucleotideo: ")
	else:
		n = input("1° nucleotideo: ")
print(soma)
