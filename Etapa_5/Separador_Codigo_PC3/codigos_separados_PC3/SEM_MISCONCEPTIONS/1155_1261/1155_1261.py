numv = int(input("copia inicial do virus: "))

numl = int(input("copia inicial de leucocitos: "))

taxav = float(input("porcentagem em: "))

taxal = float(input("porcentagem em: "))

dias = 0

while(numv>numl):
	numv = numv + (numv * (taxav/100))
	numl = numl + (numl * (taxal/100))
	dias = dias + 1

	