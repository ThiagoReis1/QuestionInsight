x = float(input("Consumo de chamadas:"))
total = float(x*0.28 + 23)
mes = (31/100)*total
total2 = total+mes

print(round(total2,2))