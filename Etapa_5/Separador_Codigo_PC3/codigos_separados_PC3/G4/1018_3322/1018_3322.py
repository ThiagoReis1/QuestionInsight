c1 = float(input("Comprimento do primeiro lado: "))
c2 = float(input("Comprimento do segundo lado: "))
custo = float(input("Custo de aplicacao: "))

area = ((c1 * c2) / 2)

print(round(custo * area, 2))