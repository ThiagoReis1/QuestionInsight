C = float(input("kWh: "))

C2 = C * 0.43+10 
ICMS = C2*(25/100)
valor = ICMS + C2


print(round(valor, 2))
