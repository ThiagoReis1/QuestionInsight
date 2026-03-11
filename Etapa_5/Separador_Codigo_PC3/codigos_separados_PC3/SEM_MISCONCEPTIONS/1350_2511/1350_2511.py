#arvores e comprimentos

from math import *

estimativa_de_arvores = float(input("Digite a quantidade de arvores: "))
comprimento_semieixo_maior = float(input("Digite o comprimento semieixo maior: "))
comprimento_do_semieixo_menor = float(input("Digite o comprimento semieixo menor: "))

area = int(pi * comprimento_semieixo_maior * comprimento_do_semieixo_menor)
quantidade_total_de_arvores = area * estimativa_de_arvores

print (int(quantidade_total_de_arvores))