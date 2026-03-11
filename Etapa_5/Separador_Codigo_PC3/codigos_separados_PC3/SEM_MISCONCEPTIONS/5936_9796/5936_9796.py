kwh = float(input("Qts kWh Meroveu consumiu em um mes: "))
conta_kwh = kwh * 0.43
valor_fixo = 10
aumento = (conta_kwh + valor_fixo) * (25/100)
conta_final = conta_kwh + valor_fixo + aumento
print(round(conta_final,2))