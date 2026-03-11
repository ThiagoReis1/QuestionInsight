peso = float(input("Qual e o peso?  "))

total1 = ((43.21 * peso) + 25)
imposto = total1 * 0.62
total2 = total1 + imposto

print(round(total2,2))