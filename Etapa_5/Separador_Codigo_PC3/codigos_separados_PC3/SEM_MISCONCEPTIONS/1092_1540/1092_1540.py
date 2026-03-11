#UNIVERSIDADE FEDERAL DO AMAZONAS
#Thiago Tuma Camilo 21600549

NUMERO = int(input("Qual o numero?"))
algarismo1 = NUMERO//100
resto_algarismo1 = NUMERO%100
algarismo2 = resto_algarismo1//10
resto_algarismo2 = resto_algarismo1%10
algarismo3 = resto_algarismo2
soma = (algarismo1**3) + (algarismo2**3) + (algarismo3**3)
if (soma == NUMERO):
	print(NUMERO,"atende a propriedade")
else:
	print(soma)
	