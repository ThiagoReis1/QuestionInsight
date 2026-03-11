volume = float(input("digite aqui o valor consumido: "))

total = volume * 0.37 + 15.0
aumento = total * (35/100)
valor = total + aumento

print(round(valor, 2))

