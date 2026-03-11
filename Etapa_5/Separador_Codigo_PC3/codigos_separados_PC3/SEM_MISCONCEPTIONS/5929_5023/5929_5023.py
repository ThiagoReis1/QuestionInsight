v = float(input("Volume de agua: "))
total = v * 0.37 + 15
total1 = (total/100) * 35
valor_total_mes = total + total1
print(round(valor_total_mes,2))