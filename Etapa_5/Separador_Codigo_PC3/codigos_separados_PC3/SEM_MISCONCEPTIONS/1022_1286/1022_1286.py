#José Carlos Gomes Pereira  -  21650882
#DATA: 16/06/2016
#Avaliação 01

from math import sqrt

aresta = float(input())
preco = float(input())

area = 2*(aresta**2)*(sqrt(2)+1)
custo = preco*area

print(round(custo,2))