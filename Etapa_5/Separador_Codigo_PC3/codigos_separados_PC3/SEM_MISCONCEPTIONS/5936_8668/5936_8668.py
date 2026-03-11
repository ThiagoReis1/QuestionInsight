
kwh = float(input("valor em kwh: "))

x = ((kwh * 0.43) + 10) 
imposto = x* 0.25
total = x + imposto
print(round(total, 2))




