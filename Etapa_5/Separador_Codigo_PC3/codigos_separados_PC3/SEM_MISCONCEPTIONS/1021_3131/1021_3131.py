aresta = float(input("comprimento da aresta: "))
custo = float(input("custo de aplicacao: "))

hexagono = (3 * (3**0.5) * (aresta ** 2)) / 2
custo_total = hexagono * custo

print(round(custo_total,2))