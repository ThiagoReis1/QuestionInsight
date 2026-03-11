popinicial = int(input(""))
taxa = float(input(""))
retirada = int(input(""))
anos = 0
t = taxa/100

while (popinicial > 0):
	popinicial = popinicial + (t * popinicial)
	popinicial = popinicial - retirada
	anos = anos + 1
print(anos)