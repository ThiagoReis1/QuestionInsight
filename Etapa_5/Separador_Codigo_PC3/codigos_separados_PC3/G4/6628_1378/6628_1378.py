# faça seu código aqui!
var = input()

i = 0
cont = 0

while i < len(var):
	if var[i].upper() == "E":
		cont += 1
	i += 1
print(cont)