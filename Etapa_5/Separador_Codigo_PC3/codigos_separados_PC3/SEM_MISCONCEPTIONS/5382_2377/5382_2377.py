from numpy import*

etiqueta = (input(""))
i = 0
varsoma = 0

while i < len (etiqueta):
	if etiqueta[i] == "A" or etiqueta[i] == "E" or etiqueta[i] == "I" or etiqueta[i] == "O" or etiqueta[i] == "U":
		varsoma = varsoma + 0.25
	else:
		varsoma = varsoma + 0.27
	i = i + 1

print(round(varsoma,2))