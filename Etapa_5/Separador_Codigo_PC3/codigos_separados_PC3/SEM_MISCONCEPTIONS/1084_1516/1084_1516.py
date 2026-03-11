prova1 = float(input("Digite o valor da prova1:"))
prova2 = float(input("Digite o valor da prova2:"))
prova3 = float(input("Digite o valor da prova3:"))
prova4 = float(input("Digite o valor da prova4:"))

media = (prova1 + prova2 + prova3 + prova4)/4

if(media >= 6):
	print(round(media,1))
	mensagem = "Aprovado"
else:
	print(round(media,1))
	mensagem = "Reprovado"
print(mensagem)