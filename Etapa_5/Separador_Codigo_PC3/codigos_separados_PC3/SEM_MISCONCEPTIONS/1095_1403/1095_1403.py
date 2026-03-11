x = int (input("Digite X: "))
resultado = ((x//10000)+(x%10000))**2
if (resultado == 9000000):
	print(resultado)
else:
	print((x//10000)**2)+((x%10000)**2)