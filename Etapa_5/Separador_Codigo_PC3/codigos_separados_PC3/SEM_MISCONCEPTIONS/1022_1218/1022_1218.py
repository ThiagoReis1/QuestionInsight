# UNIVERSIDADE FEDERAL DO AMAZONAS
# NOME: NANCY FREITAS DA SILVA
# DATA: 15/06/16
# PROGRAMA: CUSTO DE FERTILIZAÇÃO

ladoA = float(input("Digite o comprimento da aresta: "))
custo_fertilizacao = float(input("Digite o custo de fertilizacao por metro quadrado: "))
import math
metragem = (2 * ladoA **2) * (math.sqrt(2) + 1) # cálculo da área da fazenda baseada na aresta
custo_do_servico = metragem * custo_fertilizacao # cálculo do custo total do serviço de fertilização
print(round(custo_do_servico,2))