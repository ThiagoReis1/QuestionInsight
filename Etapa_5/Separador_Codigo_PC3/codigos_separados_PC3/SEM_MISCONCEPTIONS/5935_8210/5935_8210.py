peso = float(input("Peso da mercadoria: "))
valor = peso*43.21+25
val_total = valor+(valor*(62/100))
print(round(val_total,2))