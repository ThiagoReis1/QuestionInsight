energia = float(input("Quantos kWh Meroveu consumiu em um mes: "))

valorT = (energia * 0.43) + 10.00
valorT1 = (valorT * 0.25) + valorT

print(round(valorT1, 2))