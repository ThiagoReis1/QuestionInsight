C = float(input("informe o consumo de chamadas: "))
a = (0.28 * C + 23)
b = 31 / 100 * a + a

print(round(b, 2))