litros=float(input("litros abastecidos: "))

vtotal=litros*2.86 + 50.00 
icms=vtotal*(34/100)
total=vtotal+icms

print(round(total,2))