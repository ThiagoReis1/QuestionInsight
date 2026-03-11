#----------------------------------------------------------------
# UNIVERSIDADE FEDERAL DO AMAZONAS
# ANA REBECA CAVALCANTE EVANGELISTA
# MATRÍCULA: 21456290
# DATA: 16/06/2016
# OBJETIVO: Custo total de uma aplicação de fertilizante dadas
# as medidas de um terreno de area semelhante a um trapezio
#-----------------------------------------------------------------


base_maior = float(input("Valor do comprimento da base maior do terreno: ")) # em metros(m)
base_menor = float(input("Valor do comprimento da base menor do terreno: ")) # em metros(m)
altura = float(input("Valor da altura do terreno: ")) # em metros(m)
custo = float(input("Custo da aplicação do fertilizante por m²: ")) # em reais(R$)

# o resultado de (B + b) na equação da área (m) 
soma_bases = (base_maior + base_menor) 
# calculo da área do trapézio (m²)
area_tpz = (altura * soma_bases / 2 )

# valor do custo total levado em conta a area do terreno (R$/m²)
custo_total = (custo * area_tpz)

print (round(custo_total, 2))