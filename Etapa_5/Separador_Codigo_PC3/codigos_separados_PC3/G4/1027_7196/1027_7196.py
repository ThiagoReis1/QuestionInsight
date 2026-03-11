kWh = float(input("Quantos consumiu: "))



custo = (kWh * 0.43) + 10

icms = (custo/100)*25

vT = custo + icms


print(round(vT,2))