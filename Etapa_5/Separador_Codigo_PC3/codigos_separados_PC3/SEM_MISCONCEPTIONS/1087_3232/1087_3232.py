nota1 = float(input())
nota2 = float(input())
nota3 = float(input())
nota4 = float(input())

media = (nota1 + nota2 + nota3 + nota4)/4
print(round(media, 2))
if(media >= 7):
	print("Aprovado")
else:
	print("Reprovado")