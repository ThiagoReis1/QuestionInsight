valor_em_real = float(input ("Valor a trocar em Real ? "))
valor_em_real = round(valor_em_real,2)
valor_cambio = 3.96
valor_real_trocar = valor_em_real - 15.00
valor_pagar = float (valor_real_trocar / valor_cambio)
print(round(valor_pagar,2))