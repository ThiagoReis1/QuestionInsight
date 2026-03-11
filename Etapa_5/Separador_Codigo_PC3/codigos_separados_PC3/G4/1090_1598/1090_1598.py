A = float(input("Valor da compra A: "))
B = float(input("Valor da compra B: "))
C = float(input("Valor da compra C: "))
D = float(input("Valor da compra D: "))
valor = float(input("Valor limite da compra: "))



if (valor == A+B+C+D):
	print(round(A+B+C+D, 2))
	print("Sim")

else:
	print(round(A+B+C+D, 2))
	print("Nao")