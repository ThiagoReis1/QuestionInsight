from numpy import*

cont = zeros(4, dtype=int)
categorias = input("").upper().split(",")

for v in categorias:
	if v == 'A':
		cont[0] += 1
	elif v == 'B':
		cont[1] += 1
	elif v == 'L':
		cont[2] += 1
	elif v == 'H':
		cont[3] += 1
print(cont)