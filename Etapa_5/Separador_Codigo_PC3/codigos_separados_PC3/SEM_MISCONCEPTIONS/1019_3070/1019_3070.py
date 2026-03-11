largura = float(input("largura: "))
comprimento = float(input("comprimento: "))
custo = float(input("custo por metro quadrado: "))
area = largura * comprimento
custo_total = area * custo
print(round(custo_total, 2))