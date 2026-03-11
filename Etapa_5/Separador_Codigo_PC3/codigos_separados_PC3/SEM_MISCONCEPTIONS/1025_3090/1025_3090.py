largura = float(input("Largura: "))
comprimento = float(input("comprimento: "))
custo = float(input("Custo por m: "))
area = 2 * (largura + comprimento)
ct = area * custo
print(round(ct, 2))