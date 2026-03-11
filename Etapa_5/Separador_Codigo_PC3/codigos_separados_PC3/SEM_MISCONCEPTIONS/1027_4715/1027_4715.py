kwh = float(input("quantos kwh meroveu consumiu? "))
conta = float((0.43 * kwh) + 10 )
icms = float(0.25 * conta)
total =(conta + icms)
print(round(total, 2))


