from numpy import*

produto = input('Digite os produtos:').upper()

i = 0
quant = 0


while i < len(produto):
	if produto[i] == 'I':
		quant += 3.75
		
	if produto[i] == 	'M':
		quant += 4.50
		
	if produto[i] == 'S':
		quant += 2.90
		
		
	i = i + 1
	
print(round(quant, 2))