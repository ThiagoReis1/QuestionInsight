#---------------------------------------------------
# UNIVERSIDADE FEDERAL DO AMAZONAS
# Natalia de Sousa Rufino
# Data: 02/04


# Leitura da largura e comprimento da fazenda e custo do fungicida
larg = float(input('Largura da fazenda: '))
comp = float(input('Comprimento da fazenda: '))
custo = float(input('Custo do fungicida: '))

# Custo total
total = (larg * comp) * custo

print(round(total, 2))