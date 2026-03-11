altluna = 1.65
taxluna = 0.02

alt = float ( input ("digite altura: "))
tax = float ( input ("digite taxa altura: "))

tempo = 0


while alt < altluna:
	
	alt = alt + tax
	
	
	altluna = altluna + taxluna
	
	tempo = tempo + 1
	
print (tempo)