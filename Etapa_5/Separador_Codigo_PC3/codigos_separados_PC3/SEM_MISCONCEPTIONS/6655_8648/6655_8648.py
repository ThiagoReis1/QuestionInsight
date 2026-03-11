from numpy import *
#Vetores de entrada:
notas = array(eval(input("Digite as notas: ")))
peso = array([5, 1])
#Operação
multiplicacao = notas * peso
soma = sum(multiplicacao)
media_ponderada = soma / sum(peso)
#Resultado
print(round(media_ponderada, 2))