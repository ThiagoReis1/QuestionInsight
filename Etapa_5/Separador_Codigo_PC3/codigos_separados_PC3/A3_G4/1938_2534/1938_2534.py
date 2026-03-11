nome = input("Qual o aminoácido? ")

if(nome.upper() == "ARGININA"):
	peso = (6 * 12.011) + (15 * 1.00794) + (4 * 14.0067) + (2 * 15.9994)
		
if(nome == "TIROSINA"):
	peso = 9 * 12.011 + 11 * 1.00794 + 14.00674 + 3 * 15.9994
print(round(peso,2))