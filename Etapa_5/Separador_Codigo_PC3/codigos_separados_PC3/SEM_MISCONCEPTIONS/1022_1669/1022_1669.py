#Universidade Federal do Amazonas 
#ICOMP - UFAM 
#16/06/2016
#Deivison Vale - 21552110
aresta = float(input("qual o comprimento da aresta do terreno?"))
custo_fertilizacao = float(input("qual o custo da fertilizacao do terreno por metro quadrado?"))
a = float(input("inserir valor de a:"))
#verifique se as variaveis associadas ao problema sao reais ou inteiras 
#os valores em moeda devem ser arredondados em 2 casas decimais

from math import sqrt
area_do_octogono = (2 * a ** 2 *(sqrt 2 + 1))
custo_total = print(round(area_do_octogono, 2))

