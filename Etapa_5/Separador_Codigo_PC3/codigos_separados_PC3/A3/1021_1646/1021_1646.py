comprimento_da_aresta = float(input("Qual o comprimento da aresta desse terreno"))
custo_fertilizante = float(input("Qual o custo do fertilizante"))
area_hexagono = ((3 * (3**0.5)) * (comprimento_da_aresta **2 /2))
custo_total_servico = area_hexagono * custo_fertilizante
print(round(custo_total_servico,2))

minuto_excedentes = float(input("minutos excedentes por minuto"))
custo_celular = 45.00
custo_minuto = 0.97
custo_total= custo_celular