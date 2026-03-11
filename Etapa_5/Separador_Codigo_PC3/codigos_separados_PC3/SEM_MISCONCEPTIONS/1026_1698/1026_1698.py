#Marcos Felipe Melo de Lima	- 21554017
#Avaliação 01
#16/06/2016

#Entrando com variaveis
aresta = float(input("Determine o comprimento da aresta: "))
custo_metro = float(input("Qual o valor de cerca/m? "))

#Calculo do perimetro
perimetro = 6 * aresta
valor_total = perimetro * custo_metro

#Resolucao
print(round(valor_total, 2))

