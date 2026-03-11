nome = input("Qual o nome do aminoácido? ")

if(nome.upper() == "aspartato"):
	peso = (12.011 * 4) + (1.00794 * 6) + 14.0067 + (15.9994 * 4)

if(nome == "cisteina"):
	peso = (12.011 * 3) + (1.00794 * 7) + 14.0067 + (15.9994 * 2) + 32.066
print(round(peso,2))