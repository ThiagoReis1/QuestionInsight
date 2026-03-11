#-----------------------------------------------
# Nome: Ivan Lucas de Oliveira Pacheco
# Data: 21/11/2022
# Objetivo: Calcular o apotema de um poligono a partir do valor da hipotenusa
#-----------------------------------------------

# Importação de bibliotecas
from math import*

# Leitura do raio a e da quantidade de lados do poligono
raio = float(input("Qual o valor do raio? "))
n_lados = int(input("Qual a quantidade de lados do poligono? "))

# Calculo do Apotema
apotema = raio * cos(pi/n_lados)

# Imprimir o valor do Apotema
print(round(apotema,2))