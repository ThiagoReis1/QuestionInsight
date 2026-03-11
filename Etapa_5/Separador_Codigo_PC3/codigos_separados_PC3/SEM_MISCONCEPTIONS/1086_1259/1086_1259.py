#Julia Pacheco
#30 de Junho de 2016
#Av 02 - Ex 01

#ler as notas
nota1 = float(input("nota1: "))
nota2 = float(input("nota2: "))
nota3 = float(input("nota3: "))

#calculo da media
media = (nota1 + nota2+ nota3)/3

#verifica se aprovado
if(media >= 7):
	mensagem = "Aprovado"
else: mensagem = "Reprovado"

#exibe a mensagem
print(round(media,1))
print(mensagem)