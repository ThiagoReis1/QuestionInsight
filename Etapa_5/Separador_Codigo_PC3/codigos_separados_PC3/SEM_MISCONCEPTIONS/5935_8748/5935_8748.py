peso = float(input("peso da mercadoria: "))

quilo_mercadoria = peso * 43.21 + 25
total = quilo_mercadoria * 0.62
total_real = quilo_mercadoria + total

print(round(total_real,2))

