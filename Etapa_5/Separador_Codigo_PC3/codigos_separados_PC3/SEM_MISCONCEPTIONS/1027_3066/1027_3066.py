consumo = float(input("digite: "))
kWh = 0.43
valor_fixo = 10
icms = 25./100
valor_pago = (consumo * kWh + valor_fixo) * icms
print(round(valor_pago, 2))