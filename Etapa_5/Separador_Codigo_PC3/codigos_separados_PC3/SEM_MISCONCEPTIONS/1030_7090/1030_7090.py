qntdmin = float(input("Quantidade de minutos: "))

gasto = 45.0 + (qntdmin * 0.97)
porcent = gasto * 0.42
total = gasto + porcent

print(round(total,2))