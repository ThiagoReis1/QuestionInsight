qtdl = int(input("laranjas"))
lar = 0.75

if qtdl >= 6:
	lard = 0.60 * qtdl
else :
	lard = qtdl * 0.75
print(round(lard, 2))