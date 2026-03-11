nota1 = float(input("digite a 1 nota: "))
nota2 = float(input("digite a 2 nota: "))
nota3 = float(input("digite a 3 nota: "))
nota4 = float(input("digite a 4 nota: "))
ma = round((nota1 + nota2 + nota3 + nota4)/4,2)
if ma>=7:
	print(ma)
	print("Aprovado")
else:
	print(ma)
	print("Reprovado")
	