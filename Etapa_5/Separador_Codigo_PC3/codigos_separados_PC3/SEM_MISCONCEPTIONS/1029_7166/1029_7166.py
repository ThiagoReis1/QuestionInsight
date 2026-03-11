minuto = float(input("Minuto consumido: "))
mes = (minuto * 0.28) + 23.00
tarifa = mes * (31/100)
valor_pago = mes + tarifa
print(round(valor_pago, 2))