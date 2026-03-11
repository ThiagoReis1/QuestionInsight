nota1 = float(input("Digite sua primeira nota: "))
nota2 = float(input("Digite sua segunda nota: "))
nota3 = float(input("Digite sua terceira nota: "))

media = (nota1 + nota2 + nota3) / 3

if (media >= 6):
	mensagem = "Aprovacao"
else:
	mensagem = "Reprovacao"
from math import *	
print(round(media,2))
print(mensagem)