peso = float(input("racao peso: "))
quant = float(input("racao quantidade: "))

resto_racao = peso - (quant * 7)

print(round(resto_racao, 3))