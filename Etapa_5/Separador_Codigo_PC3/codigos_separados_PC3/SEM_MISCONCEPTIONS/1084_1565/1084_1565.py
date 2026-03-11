from math import*

nota = float(input("Digite o valor da nota:"))
nota2 = float(input("Digite o valor da nota:"))
nota3 = float(input("Digite o valor da nota:"))
nota4 = float(input("Digite o valor da nota:"))

soma = (nota + nota2 + nota3 + nota4)
media = (soma/4)
print (round(media,1))
if(media >= 6):
	print ("Aprovado")
else:
	print("Reprovado")