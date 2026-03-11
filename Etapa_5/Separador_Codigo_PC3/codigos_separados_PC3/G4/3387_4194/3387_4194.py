un = input("Unidade em que a medida esta (M) ou (K): ").upper()
kl = float(input("Valor da medida: "))


if( un == "K"):
	x = 2.35215 * kl
else:
	x = kl / 2.35215 
print(round(x, 2))