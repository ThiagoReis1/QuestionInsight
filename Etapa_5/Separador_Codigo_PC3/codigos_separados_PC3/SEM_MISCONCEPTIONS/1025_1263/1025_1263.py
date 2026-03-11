# andrea cristina de lima lopes
# matricula- 21552445	
# avaliacao - 01

# comando de entrada do valor do lado menor 
largura_A = float(input())

# comando de entrada do valor de lado maior
comprimento_a = float(input())

# formula de calculo do perimetro
per = 2 * ( largura_A + comprimento_a)

# valor po m2
custo_m = float(input())

# calculo do custo total
custo_total = per * custo_m

# print(round(per, 2))
print(round(custo_total, 2))
