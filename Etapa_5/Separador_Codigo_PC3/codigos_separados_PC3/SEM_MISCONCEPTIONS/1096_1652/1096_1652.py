#################################################
# UFAM - UNIVERSIDADE FEDERAL DO AMAZONAS
# RODRIGO FONTANELLA CESTARI
# 30/06/2016
# OBJETIVO: Elabore um programa que verifique se 
# um numero fornecido pelo usuario satisfaz essa 
# caracteristica (165033 = 16³ + 50³ + 33³).
#################################################
# numero a ser digitado
numero = int(input("Qual o numero voce deseja inserir? "))

#separaçao dos numeros em duas unidades
valor1 = numero // 10000
resto1 = numero % 10000
valor2 = resto1 // 100
resto2 = resto1 % 100
valor3 = resto2
#resultado dos valores separados elevado ao cubo
resultado = (valor1 ** 3) + (valor2 ** 3) + (valor3 **3)
#condicao
if (numero == resultado):
	print ((numero),"atende a propriedade")
else:
	print (resultado)
