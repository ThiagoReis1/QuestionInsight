
kwhMes = float(input("Kwh consumido no mes: "))
conta = kwhMes * 0.43 + 10.00
total = conta * (25 / 100) + conta 

print(round(total, 2))
