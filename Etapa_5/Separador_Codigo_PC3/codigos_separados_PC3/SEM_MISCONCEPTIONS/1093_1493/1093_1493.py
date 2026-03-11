# UNIVERSIDADE FEDERAL DO AMAZONAS
# AVALIAÇÃO PARCIAL 2
#Michael Evangelista da Cruz
# Engenharia Quimica 
# 07/07/2016

numero = int(input("Digite um numero de 4 digitos: "))

parcela_1 = numero // 100
parcela_2 = numero % 100

if(numero == parcela_1 ** 2 + parcela_2 ** 2):
	print(numero, "atende a propriedade")
	
else: 
	print(parcela_1**2 + parcela_2**2)