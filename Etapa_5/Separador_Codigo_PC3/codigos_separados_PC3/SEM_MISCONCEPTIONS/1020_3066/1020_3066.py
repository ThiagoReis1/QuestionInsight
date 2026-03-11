base_maior = float(input("digite: "))
base_menor = float(input("digite: "))
altura = float(input("digite: "))
custo = float(input("digite: "))
area = altura * (base_maior + base_menor) / 2
custo_total = area * custo
print(round(custo_total, 2))