#UNIVERSIDADE FEDERAL DO AMAZONAS
#ENGENHARIA QUIMICA
#MICHAEL EVANGELISTA DA CRUZ - 21600845
#DATA: 05/08/2016
#AVALIACAO PARCIAL 04

Popinicial = int(input("Qual a população inicial: "))
taxacresc = int(input("Qual a taxa de crescimento: "))
retiradaanual = int(input("Qual a retirada anual: "))

contador = 0
soma = Popinicial

while(soma > 0):
	soma = (soma + (soma * taxacresc/100)) - retiradaanual
	
	contador = contador + 1
	
print(contador)

