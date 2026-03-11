nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
nota3 = float(input("Digite a terceira nota: "))
nota4 = float(input("Digite a quarta nota: "))

MA = (nota1 + nota2 + nota3 + nota4) / 4

if (MA >= 7.0):
	print(round(MA , 2))
	print("Aprovado")
else:
	print(round(MA , 2))
	print("Reprovado")