#UNIVERSIDADE FEDERAL DO AMAZONAS
#INTRODUÇAO A PROGRAMAÇÃO DE COMPUTADORES
#YAGO PEREIRA DE SOUZA - 21850592
#ENGENHARIA DE MATERIAIS
#SEG E QUA: 14H AS 16H

from math import*

CA=float(input("Digite o comprimento da aresta dessa fazenda: "))
CS=float(input("Digite custo de aplicacao: "))

CT=((2*(CA**2)) * ((sqrt(2)) + 1))
CP= CT*CS

print(round(CP, 2))
