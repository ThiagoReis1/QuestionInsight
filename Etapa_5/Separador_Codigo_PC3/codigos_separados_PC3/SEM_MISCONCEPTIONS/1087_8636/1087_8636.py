nota1= float(input("nota 1: "))
nota2= float(input("nota 2: "))
nota3= float(input("nota 3: "))
nota4= float(input("nota 4: "))

m = ((nota1 + nota2 + nota3 + nota4) / 4)

if m >= 7:
	print(round(m, 2))
	print("Aprovado")
else:
	print(round(m, 2))
	print("Reprovado")
	