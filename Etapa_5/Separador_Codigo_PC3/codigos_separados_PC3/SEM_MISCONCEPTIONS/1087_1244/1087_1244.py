#Kamila Dias Pereira
# Avaliação 2

Av1 = float(input("Digite nota 1: "))
Av2 = float(input("Digite nota 2: "))
Av3 = float(input("Digite nota 3: "))
Av4 = float(input("Digite nota 4: "))

media = (Av1 + Av2 + Av3 + Av4)/4
mediaav = (media ,2)
print(mediaav)

if (media >= 7.0):
	mensagem = ("Aprovado")
	print(mensagem)
			
else:
	mensagem = ("Reprovado")
	print(mensagem)