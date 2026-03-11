pvi = int(input("Pontos de vida inicial: "))
d1 = int(input("Dado 1: "))
d2 = int(input("Dado 2: "))
d3 = int(input("Dado 3: "))

N = (d1 + d2 + d3)

pvr = ((pvi) - (10*N))

if (pvr > 0):
	print("VIVO")
else:
	print(pvr)
	print("MORTO")