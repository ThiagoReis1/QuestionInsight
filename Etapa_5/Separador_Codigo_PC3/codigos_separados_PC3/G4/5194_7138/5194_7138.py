c = input("QUAL A CLASSIFICACAO DA MISSAO (A/B)? ")
vl = float(input("QUAL O VALOR PAGO PELA MISSAO? "))

if(c.upper() == "A"):
	classe = "Jounin"
	pg = vl - (vl*(22/100))
else:
	classe = "Chunin"
	pg = vl - (vl*(15/100))
	
print("Classe:",classe)
print(round(pg, 2))