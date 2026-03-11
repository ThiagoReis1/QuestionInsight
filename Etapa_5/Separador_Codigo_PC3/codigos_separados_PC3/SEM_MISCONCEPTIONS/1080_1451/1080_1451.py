prova1 = float(input("Digite a nota da prova1: "))
prova2 = float(input("Digite a nota da prova2: "))
prova3 = float(input("Digite a nota da prova3: "))
soma = prova1 + prova2 + prova3
media = soma / 3
if ( media >= 5):
	mensagem = 'Aprovado'
else:
	mensagem = 'Reprovado'
print(round(media,1))
print(mensagem)