comb = input('A ou B ou c?')
qnt = int(input('quantos?'))

if comb.upper() == 'A' :
	print(round(qnt * 30,2))
	
if comb.upper() == 'B' :
	print(round(qnt * 30,2))
	
if comb.upper() == 'C' :
	a = (qnt * 30) * 15/100
	b = (qnt * 30) - a
	print(round(b,2))
