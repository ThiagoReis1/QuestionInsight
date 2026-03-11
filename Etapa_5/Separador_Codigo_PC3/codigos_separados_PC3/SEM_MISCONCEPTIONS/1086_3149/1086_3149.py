nota1 = float(input("Nota 1:"))
nota2 = float(input("Nota 2:"))
nota3 = float(input("Nota 3:"))

m = (nota1 + nota2 + nota3) / 3
if(m >= 7):
	print(round(m, 1))
	print("Aprovado")
else:
	print(round(m, 1))
	print("Reprovado")