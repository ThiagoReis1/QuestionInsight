tax = 25.00

kg = float(input("Informe o peso da mercadoria: "))

value = (kg * 43.21) + tax

icms = value*62/100

total = value + icms

print(round(total, 2))