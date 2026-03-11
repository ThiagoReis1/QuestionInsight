escala = input("escala de temperatura:")
valor = float(input("valor da temperatura:"))
K = round(valor + 273.15, 2)
C = round(valor - 273.15, 2)
if (escala == "C"):
	print(K)
else:
	print(C)