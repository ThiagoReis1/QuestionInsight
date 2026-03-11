# Universidade Federal do Amazonas
# Thais de Almeida Ferreira
# 2155375
# Avaliacao 1
#16/06/2016

aresta = float(input("Qual o comprimero da aresta?"))
area = (2 * aresta**2*(2**0.5 + 1)) 

custo = float(input("Qual o custo de aplicação?"))
custo_total = area * custo
print(round(custo_total, 2))
