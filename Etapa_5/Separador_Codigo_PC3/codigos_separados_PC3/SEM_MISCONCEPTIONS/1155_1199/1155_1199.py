numvirus = int(input("Insira as unidades de virus presentes: "))
numlcts = int(input("Insira as unidades de leucocitos presentes: "))
taxavirusdia = float(input("Insira a taxa de multiplicacao do virus por dia: "))
taxalctsdia = float(input("Insira a taxa de multiplicacao dos leucocitos por dia: "))
diasparacura = 0

taxavirusdia = taxavirusdia/100
taxalctsdia = taxalctsdia/100

while ((2*numlcts) != numvirus ):
	numvirus = numvirus * taxavirusdia
	numlcts = numlcts * taxalctsdia
	diasparacura = diasparacura + 1

print(diasparacura)
	
