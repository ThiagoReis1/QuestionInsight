vol_agua = float(input("volume de agua consumida: "))
pagar_agua = (vol_agua*0.37)+15.00
icms = pagar_agua*0.35
valor_pago = pagar_agua+icms
print(round(valor_pago, 2))
