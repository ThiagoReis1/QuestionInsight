agua = float(input("Informe o volume de agua consumido durante o mes: "))

valor = (agua*0.37)+15.00
icms = valor+(valor*(35/100))

print(round(icms, 2))