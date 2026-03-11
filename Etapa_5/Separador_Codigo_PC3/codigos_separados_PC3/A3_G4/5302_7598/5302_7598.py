m = int(input("massa"))
qtd = int(input("quantidade de anos"))

i = 1
anos = 0

while (anos < qtd):
	anos = anos + 1
	m = m - (m*5/100)	
	
	print(round(m , 2))