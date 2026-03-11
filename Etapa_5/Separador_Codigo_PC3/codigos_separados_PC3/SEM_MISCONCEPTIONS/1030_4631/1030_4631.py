x = float(input("Minutos excedidos. "))

plano = 45 + 0.97 * x 
total = plano + 0.42 * plano

print(round(total,2))