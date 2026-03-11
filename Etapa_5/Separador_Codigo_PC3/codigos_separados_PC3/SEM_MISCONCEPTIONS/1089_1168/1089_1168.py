compra1 = float(input("valor da primeira compra: "))
compra2 = float(input("valor da segunda compra: "))
compra3 = float(input("valor da terceira compra: "))
limi = float(input("valor do limite: "))
tot = compra1 + compra2 + compra3
if (tot <= limi):
   print(tot)
   print("Sim")
else:
	print(tot)
	print("Nao")
	