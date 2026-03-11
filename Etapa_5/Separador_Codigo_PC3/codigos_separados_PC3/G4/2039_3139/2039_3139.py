dna = input("quatro nucleotideos: ").upper()


cont = 0
while (dna != "S") and (dna =="A" or dna =="G" or dna == "C" or dna == "T"):
	if (dna == "A"):
		cont = cont + 1
	
	dna = input("quatro nucleotideos: ").upper()
print(cont)