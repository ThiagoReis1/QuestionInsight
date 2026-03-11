#biscoito 3.75
#cereal 7.90
#enlatados 9.85

compras = input()
i=0
soma =0
while i<len(compras):
	if compras[i] == 'B':
		soma+=3.75
	elif compras[i] == 'C':
		soma+=7.90
	elif compras[i] == 'E':
		soma+=9.85
		
	i+=1
	
print(round(soma,2))	
	