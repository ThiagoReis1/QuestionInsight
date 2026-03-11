nota1 = float(input("nota1: "))
nota2 = float(input("nota2: "))
nota3 = float(input("nota3: "))
resultado = (nota1 + nota2 + nota3)/3
print(round(resultado, 1))
if(resultado >= 7.0):
	print("Aprovado")
else:
	print("Reprovado")

