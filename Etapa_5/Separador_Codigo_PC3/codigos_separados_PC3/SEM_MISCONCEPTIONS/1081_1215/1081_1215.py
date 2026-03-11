from math import*
a = float(input("digite a nota da prova 1:"))
b = float(input("digite a nota da prova 2:"))
c = float(input("digite a nota da prova 3:"))
d = float(input("digite a nota da prova 4:"))

media = ((a + b + c + d) / 4)

if (media >= 5):
	mensagem = "Aprovacao"
else:
	mensagem = "Reprovacao"

print(round(media, 2))
print(mensagem)

