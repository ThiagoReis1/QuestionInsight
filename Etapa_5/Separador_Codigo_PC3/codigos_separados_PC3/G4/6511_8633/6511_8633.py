o = input("tipo de entrada (A,B,C,D ou E): ")
a = int(input("quantidades desejadas: "))

valor = 25.90 * a
desc = valor * 0.10

if (o == 'B'):
	valor = valor - desc

print(round(valor, 2))
	

