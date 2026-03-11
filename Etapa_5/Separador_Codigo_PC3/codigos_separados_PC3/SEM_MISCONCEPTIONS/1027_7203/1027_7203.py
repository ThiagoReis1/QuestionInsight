gasto = float(input("Valor gasto: "))
kWh = 0.43
vf = 10
icms = 0.25*(gasto*kWh+vf)
valorTotal = (gasto*kWh+vf+icms)
print(round(valorTotal,2))

