KW = float(input("Consumo mensal de kWh: "))

VF = 10
KWH = 0.43
V = KW * KWH + VF
Tt = V + V * 25/100

print(round(Tt, 2))