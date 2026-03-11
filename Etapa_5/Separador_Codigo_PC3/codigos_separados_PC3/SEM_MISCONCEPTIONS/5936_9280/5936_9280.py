valfixo = 10
consumokwh = float(input("digite o consumo kWh no mes: "))
t = (consumokwh * 0.43) + valfixo
x = t * (25 / 100)
valorpago = t + x
print("o valor total a ser pago e:")
print(round(valorpago,2))