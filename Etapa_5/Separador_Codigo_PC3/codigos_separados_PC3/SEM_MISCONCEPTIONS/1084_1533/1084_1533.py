nota1 = float(input("digite a nota 1 "))
nota2 = float(input("digite a nota 2 "))
nota3 = float(input("digite a nota 3 "))
nota4 = float(input("digite a nota 4 "))
R = (nota1 + nota2 + nota3 + nota4) / 4
print(round(R , 1))
if ( R >= 6):
	print("Aprovado")
else:
	print("Reprovado")