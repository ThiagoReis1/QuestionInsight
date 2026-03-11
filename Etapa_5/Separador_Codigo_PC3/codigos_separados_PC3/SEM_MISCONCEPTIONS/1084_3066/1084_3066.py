nota1 = float(input("digite: "))
nota2 = float(input("digite: "))
nota3 = float(input("digite: "))
nota4 = float(input("digite: "))
divisao = 4
media = (nota1 + nota2 + nota3 + nota4) / divisao

if(media >= 6.0):

	mensagem = "Aprovado"
else:
	mensagem = "Reprovado"
print(round(media, 1))
print(mensagem)