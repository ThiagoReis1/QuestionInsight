aresta = float(input("Lado da cerca(metros): "))
custo_metro = float(input("Custo por metro: RS"))

custo_total = custo_metro * (aresta * 6) 
print(round(custo_total,2))