# Variáveis geral

d = int(input())

# Variáveis laço

lanc = 0 # lancamentos do dados
lanc6 = 0 # lancamentos em 6

while (d != -1):
	
	if (d == 6):
		
		lanc6 = lanc6 + 1
		
	
	lanc = lanc + 1
	
	d = int (input())

print (lanc)
por = (lanc6 * 100)/lanc
print (round(por, 2))