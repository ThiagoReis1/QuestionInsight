notas = input("digite: ")

cont = [0 ,0 ,0 ,0]
notasl = notas.split(",")

for i in notasl:
	if i == "C":
		cont[0] += 1
	if i == "D":
		cont[1] += 1
	if i == "V":
		cont[2] += 1
	if i == "U":
		cont[3] += 1

print((cont))