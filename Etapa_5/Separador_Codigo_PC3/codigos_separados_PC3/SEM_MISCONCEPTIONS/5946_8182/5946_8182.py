lanche = input("Escreva L/P: ")
qlp = int(input("quantidade: "))
qf = int(input("quantidade de refri: "))
qf1 = qf * 3

if (lanche == "P"):
	resultado = qlp * 4.50 + qf1
	print(round(resultado,2))

else:
	resultado = qlp * 6.00 + qf1
	print(round(resultado,2))