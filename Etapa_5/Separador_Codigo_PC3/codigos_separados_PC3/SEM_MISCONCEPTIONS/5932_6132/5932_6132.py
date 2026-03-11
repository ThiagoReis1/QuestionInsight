a = float(input("consumo: "))                 #consumo de chamadas durante certo mes

vm = (a * 0.28) + 23.00
imposto = vm * 31/100
total = vm + imposto
print(round(total,2))
