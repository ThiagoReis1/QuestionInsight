from numpy import*
abc = input(":").upper()
valor =0
for caractere in abc:
	if caractere in "AEIOU":
		valor += 3.15
	else:
		valor +=4.17
		
	
print(round(valor,2))

	