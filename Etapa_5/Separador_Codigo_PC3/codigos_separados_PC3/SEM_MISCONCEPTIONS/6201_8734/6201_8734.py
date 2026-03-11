altura = 1.77
taxa = 0.02

faltura = float(input('a'))
ttaxa = float(input('a'))

a = 0

while (faltura < altura):
	altura += taxa
	faltura += ttaxa
	a += 1 
	
print(a)
	