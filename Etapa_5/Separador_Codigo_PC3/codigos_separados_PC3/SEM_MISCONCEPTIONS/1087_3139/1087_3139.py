nota1 = float(input("nota 1: "))
nota2 = float(input("nota 2: "))
nota3 = float(input("nota 3: "))
nota4 = float(input("nota 4: "))

x = (nota1 + nota2 + nota3 + nota4) / 4

if (x >= 7):
	msg = "Aprovado"
else:
	msg = "Reprovado"
	
print(round(x, 2))
print(msg)