c = (input("Digite (p/s): ").upper()
p = float(input("Valor do emprestimo: "))
j = p * r

if c == "P":
	r = 0.09
else:
	r = 0.11

print(round(j, 2))