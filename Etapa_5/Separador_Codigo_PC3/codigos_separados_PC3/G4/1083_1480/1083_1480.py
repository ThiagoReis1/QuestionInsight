#Universidade Federal do Amazonas 
#Laboratório de codificação 02
#PROVA
#Engenharia Quiímica
#Pedro Vinícius Borges de Souza - 21650221

x = float(input("diga uma nota: "))
y = float(input("diga uma nota: "))
z = float(input("diga uma nota: "))

if(( x + y + z)/3 >= 6):
	mensagem = "Aprovacao"
else:
	mensagem = "Reprovacao"
print(mensagem)
 