# Victor Chaves

t = float(input("Digite o consumo de chamadas em minutos:"))

valor = (0.28 * t + 23) * (1 + (31/100))

total = round(valor, 2)

print(total)