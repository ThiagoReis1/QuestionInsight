prova1 = float(input("nota 1:"))
prova2 = float(input("nota 2:"))
prova3 = float(input("nota 3:"))
prova4 = float(input("nota 4:"))
prova5 = float(input("nota 5:"))
media = (prova1 + prova2 + prova3 + prova4 + prova5) // 5
aprovado = media >= 5
reprovado = media < 5
if( media >= 5):
	mensagem(aprovado)
else:
	mensagem(reprovado)
print(round(media,1))
print(mensagem)
