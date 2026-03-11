custo_por_m = 0.37
valor_fixo = 15
custo_mensal = float(input("digite o valor consumido durante um mes = "))
subtotal= custo_por_m + valor_fixo 
icms = 35
custo_total = subtotal + (35/100 * 100) + subtotal + 4.5
print(round(custo_total))