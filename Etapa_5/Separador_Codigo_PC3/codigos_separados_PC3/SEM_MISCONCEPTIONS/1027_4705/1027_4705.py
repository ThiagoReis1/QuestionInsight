kwh = float(input("quantos kwh foram usados."))
total = kwh * 0.43
vlr = total + 10.00
cobb = (25 * vlr) / 100
cobb3 = cobb + vlr
print(round(cobb3, 2))
