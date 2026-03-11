comp_aresta = float(input("Comprimento da aresta do terreno?"))
custo_por_m2 = float(input("Custo de construção da cerca por m2?"))
a = comp_aresta
perimetro_hex = 6 * a
valor_total = (custo_por_m2 * perimetro_hex)
print(round(valor_total, 2))