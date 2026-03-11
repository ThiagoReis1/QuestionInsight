consumo_p_m = float(input("Consumo de chamada por minuto: "))

consumo_por_mes = consumo_p_m * 0.28 + 23.00
total = consumo_por_mes * 31/100 + consumo_por_mes

print(round(total, 2))






