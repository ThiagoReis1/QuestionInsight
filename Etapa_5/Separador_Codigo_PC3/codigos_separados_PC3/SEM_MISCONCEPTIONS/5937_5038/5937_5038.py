litros_abastecido = float(input("litros: "))
g = 2.86
t = 50.00
total = g * litros_abastecido + t
a = total*0.34
imposto = a + total
print(round(imposto,2))