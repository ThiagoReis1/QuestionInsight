#Elysmara Coutinho de oliveia
#data:16/06/2016
#avaliação
from math import pi
a=float(input("escreva aqui o raio da fazenda:")) # a é o raio da fazenda
custo_fertilizante=float(input("escreva aqui o custo da aplicação do fertilizante:"))

custo_total=custo_fertilizante*pi*a**2

print(round(custo_total,2))