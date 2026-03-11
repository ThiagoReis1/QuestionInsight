peso_merc = float(input("digite o peso da mercadoria:"))
icms = (peso_merc*43.21+25)*0.62
total = (peso_merc*43.21+25)+icms
print(round(total,1))