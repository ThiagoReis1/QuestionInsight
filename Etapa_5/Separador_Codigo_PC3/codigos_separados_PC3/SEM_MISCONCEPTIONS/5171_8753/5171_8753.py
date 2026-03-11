peso = float(input("peso em gramas: "))
quant = float(input("quant diaria em gramas: "))
total = peso - (quant * 7)
print(round(total, 2))