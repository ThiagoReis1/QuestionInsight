tjg = float(input(": "))
taxa = float(input(": "))
alluna = 1.65
taxluna = 0.02
gato = 0
while (tjg <= alluna):
	alluna = alluna + taxluna
	tjg = tjg + taxa
	gato = gato + 1
print(gato)
