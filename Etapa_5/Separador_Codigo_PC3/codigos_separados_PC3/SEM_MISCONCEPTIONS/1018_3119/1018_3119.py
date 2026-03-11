comprimento_a = float(input("comprimento do primeiro cateto: "))
comprimento_b = float(input("comprimento do segundo cateto: "))
custo = float(input("custo por m2: "))

area = comprimento_a * comprimento_b / 2

custo_total = area * custo

print(round(custo_total, 2 ))