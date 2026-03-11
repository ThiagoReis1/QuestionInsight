nota1 = float(input("digite a nota: "))
nota2 = float(input("digite a nota: "))
nota3 = float(input("digite a nota: "))
nota4 = float(input("digite a nota: "))
media = (nota1 + nota2 + nota3 + nota4)/4
print(round(media, 1))
if (media >= 6.0):
 	print("Aprovado")
else:
 	print("Reprovado")
