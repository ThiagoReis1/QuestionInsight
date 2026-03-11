var1 = int(input("faces "))

cont = 0
aux = 0

while var1 != -1:
	aux = aux + 1
	if var1 == 5:
		cont = cont + 1
	var1 = int(input("faces "))
print(aux)

y = (cont * 100)/aux
print(y)