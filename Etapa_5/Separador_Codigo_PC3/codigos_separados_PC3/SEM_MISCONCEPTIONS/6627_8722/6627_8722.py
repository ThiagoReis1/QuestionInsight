# faça seu código aqui!
ferrou = input("Digite: ").upper()
i = 0
d = 0

while i < len(ferrou):
	if ferrou[i] == "D":
		d += 1
	i += 1
	
print(d)