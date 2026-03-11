#---------------------------------------------------------
# Nome: Ivan Lucas de Oliveira Pacheco
# Data: 11/01/2023
# Objetivo: Calcular o valor da série matematica para o numero real X até K termos
#---------------------------------------------------------

# Definição das variaveis acumuladora e contadora
n = 0
soma = 0

variavel_x = float(input("Qual o numero da serie? "))
termos = int(input("Digite a quantidade de termos da serie: "))

while (n < termos):
	soma = soma + (variavel_x / ((2 * n) + 1))
	n = n +1

print (round(soma,8))
	