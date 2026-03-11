peso = float(input("Qual o peso da mercadoria a ser transportada: "))

v = peso * 43.21 + 25
t = v + v * (62/100)

print(round(t, 2))
