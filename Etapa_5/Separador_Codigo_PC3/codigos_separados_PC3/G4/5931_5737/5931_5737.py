q = float(input("Quantidade de minutos: "))

p = 45.00
e = 0.97 * q

t = p + e
icms = (t * 42)/100
total = t + icms



print(round(total,2))