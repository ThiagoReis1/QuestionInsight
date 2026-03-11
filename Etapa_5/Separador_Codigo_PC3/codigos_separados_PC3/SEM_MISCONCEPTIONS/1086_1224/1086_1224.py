nota1 = float(input("digite a primeira nota"))
nota2 = float(input("digite a segunda nota"))
nota3 = float(input("digite a terceira nota"))
media = (nota1 + nota2 + nota3) / 3
print(round(media, 1))
if (media >= 7):
	print("Aprovado")
else:
	print("Reprovado")