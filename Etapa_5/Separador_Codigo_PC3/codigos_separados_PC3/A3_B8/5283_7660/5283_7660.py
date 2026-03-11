#-----------------------------------------------------------------------
# Nome: Ivan  Lucas de Oliveira Pacheco
# Data: 11/01/2023
# Objetivo: Calcular o percetual de numeros negativos e numeros positivos digitados
#-----------------------------------------------------------------------

# Definição de variaveis contadoras (quantidade de numeros digitados)
positivos = 0
negativos = 0
total = 0

# Set de variável para entrada em loop
num = 1

while (num != 0):
	num = int(input("Digite um numero inteiro: "))
	if num > 0:
		positivos = positivos + 1
		total = total + 1
	elif num < 0:
#		negativos = negativos + 1
		total = total +1
		
# perc_neg = negativos / total
perc_positivos = (positivos / total) * 100

print (total)
print (round(perc_positivos,2))