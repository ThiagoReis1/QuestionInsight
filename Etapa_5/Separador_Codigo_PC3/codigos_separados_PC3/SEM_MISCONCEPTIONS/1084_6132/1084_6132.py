nota1 = float(input("insira a nota 1: "))
nota2 = float(input("insira a nota 2: "))
nota3 = float(input("insira a nota 3: "))
nota4 = float(input("insira a nota 4:"))

media = (nota1 + nota2 + nota3 + nota4)/4
print(round(media,1))

if media >= 6.0:
	print("Aprovado")
else:
	print("Reprovado")