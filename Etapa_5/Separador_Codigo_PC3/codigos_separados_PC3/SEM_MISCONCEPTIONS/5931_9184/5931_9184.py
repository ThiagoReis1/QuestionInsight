minutos = float(input("Digite um valor: "))

mensal = 45 + 0.97 * minutos

total = mensal + (42 / 100) * mensal

print(round(total, 2))