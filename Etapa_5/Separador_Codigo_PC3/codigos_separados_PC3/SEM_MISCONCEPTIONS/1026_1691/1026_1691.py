aresta = float (input ("Valor aresta ? "))
custo_metro_linear = float (input ("Valor Metro ? "))
perimetro = 6*aresta
custo_total = perimetro*custo_metro_linear
print(round(custo_total,2))