agua_consumida = float(input("informe o volume de agua consumida"))
custo_basico = agua_consumida * 0.37 +15
icms = 35 * custo_basico
icms = icms / 100
custo_total = custo_basico + icms
print (round(custo_total, 2))



