kw = float(input("quantidade de kwh consumido: "))
valor_cons = 0.43*kw + 10
valor_a_ser_pago =valor_cons + valor_cons * (25/100)
print(round(valor_a_ser_pago,2))