numero_x = int(input("Numero de x: "))
numero_y = int(input("Numero de y: "))

soma = 0
contador = numero_x

while contador <= numero_y:
	if contador % 7 == 0:
		soma = soma + contador
	contador = contador + 1
print(soma)