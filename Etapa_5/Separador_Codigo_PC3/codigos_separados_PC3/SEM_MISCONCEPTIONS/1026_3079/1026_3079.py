lado_terreno = float(input())
custo = float(input())

perimetro_terreno = (lado_terreno)*6

custo_total = perimetro_terreno * custo

print(round(custo_total,2))