a = float(input("quantidade de tambaqui?"))
b = float(input("quantidade de pacu?"))
txa = float(input("qual a taxa do tambaqui?"))
txb = float(input("qual a taxa do pacu?"))
c = float(input("numero maximo?"))
anos = 1
while((a + b) < c):
	crescimento = a * (txa/100)
	a = a + crescimento
	crescimentob = b * (txb/100)
	b = b + crescimentob
	c = a + b
	anos = anos + 5
print(anos)	
	

	
	
	
