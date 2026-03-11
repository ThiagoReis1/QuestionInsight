var1 = float(input("Digite o peso da mercadoria: "))
porc = 62
total = (var1 * 43.21 + 25.0)
total2 = (total + (total * porc / 100))
print (round(total2,2))
