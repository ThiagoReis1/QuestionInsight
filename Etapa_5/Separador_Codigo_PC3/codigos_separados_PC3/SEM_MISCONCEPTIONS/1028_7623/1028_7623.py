volume = float(input(" Insira o volume da agua consumida durante o mes "))

valor = (volume * 0.37 + 15)
icms = valor * 0.35

total = valor + icms

print(round(total, 2))