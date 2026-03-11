a = float(input("comprimento: "))
ap = float(input("fertilizante: "))
area = 3 * 3 ** 0.5 * (a ** 2) / 2
custo = area * ap
print(round(custo, 2))