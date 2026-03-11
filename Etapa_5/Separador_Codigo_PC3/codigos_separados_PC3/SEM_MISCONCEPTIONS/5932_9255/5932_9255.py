c = float(input("Consumo de chamada: "))
calls = c * 0.28 + 23
total = calls + 0.31 * calls
print(round(total, 2))