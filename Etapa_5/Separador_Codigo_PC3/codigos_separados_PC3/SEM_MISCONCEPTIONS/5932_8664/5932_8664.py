
consumo = float(input("Qual o consumo de chamadas por mes? "))

plano = consumo*0.28 + 23.00
icms = plano*(31/100)

print(round(plano+icms, 2))