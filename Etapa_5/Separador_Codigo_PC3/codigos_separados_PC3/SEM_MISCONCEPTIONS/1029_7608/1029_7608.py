consumo = float(input("Consumo em minutos por mes: "))
valor = 0.28 * consumo 
fixo = 23
valor_total = valor + fixo
icms = valor_total * 0.31
total = valor + icms + fixo
print(round(total, 2))