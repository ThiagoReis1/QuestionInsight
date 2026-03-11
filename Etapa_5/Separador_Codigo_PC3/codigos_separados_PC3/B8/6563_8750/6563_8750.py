# faça seu código aqui!
d = int(input("quantidade de dias reservados: "))

if (d < 15):
	valor = 175.00*d+20.00
	print("total=", valor)
elif (d == 15):
	valor = 175.00*15+16.00
	print("total=", valor)
elif (d > 15):
	valor = 175.00*d+10.00
	print("total=", valor)