consumo = float(input("total de minutos:"))


plano= float(0.28) * consumo + 23.00

icms=plano*31/100

calculo=plano+icms

print(round(calculo,2))