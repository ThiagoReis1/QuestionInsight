# Entrada: Molécula
m = input("Nome do aminoácido: ").lower()

# Pesos Moleculares
O = 15.9994
C = 12.011
N = 14.00674
H = 1.0079

# Equações Químicas
hi = C*6 + H*10 + N*3 + O*2
le = C*6 + H*13 + N + O*2
li = C*6 + H*15 + N*2 + O*2

# Condições
if (m == "histidina"):
	print(round(hi,2))
elif (m == "leucina"):
	print(round(le,2))
elif (m == "lisina"):
	print(round(li,2))
else:
	print("Entrada:",m)
	print("Dado Invalido")