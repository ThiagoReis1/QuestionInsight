import math 
#Ler valores:
comp_aresta = float(input("Digite comprimento aresta: "))
custo_m2 = float(input("Digite o custo do m2: "))

#Computar area 

Area = 3*math.sqrt(3)*math.pow(comp_aresta,2)*(0.5)

custo_total = Area*custo_m2

rounded = round(custo_total,2)

print(rounded)