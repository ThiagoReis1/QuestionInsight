cons = float(input("Informe o valor de consumo de chamadas: "))

a = (cons * 0.28) + 23
b = a + (a*(31/100))

print(round(b, 2))