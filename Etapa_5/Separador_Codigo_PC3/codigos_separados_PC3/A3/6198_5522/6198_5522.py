alt_luna = 1.65
taxa_luna = 0.02
txc = 0.02
alt = float(input())
taxa = float(input())
ano = 0
while alt <= alt_luna:	
	alt_luna += taxa_luna
	alt += taxa
	ano += 1
print(ano)