#Universidade Federal do Amazonas - UFAM
#Igor R Chicolet da Silva
#Matricula: 21204615
#Avaliacao 1 - Ex. 02

taxa = 9.00
conv_peso_arg = 0.26
valor_reais = float

valor_reais = float(input("Qual a quantia em reais? "))
peso_arg = (valor_reais - taxa) / conv_peso_arg

print(round(peso_arg,2))
