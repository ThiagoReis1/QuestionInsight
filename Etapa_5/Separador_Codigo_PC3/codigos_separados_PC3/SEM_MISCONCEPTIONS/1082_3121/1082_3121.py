prova1 = float(input("valor: "))
prova2 = float(input("valor: "))
prova3 = float(input("valor: "))
prova4 = float(input("valor: "))
prova5 = float(input("valor: "))

media=(prova1+prova2+prova3+prova4+prova5)/5

if (media>=5):
	mensagem=("Aprovado")
else:
	mensagem=("Reprovado")
print(round(media, 1))		
print(mensagem)