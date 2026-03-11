altura_bia = 1.69
taxa_bia = 0.01

alt = float(input(''))
taxa = float(input(''))

ano = 0 

while(alt < altura_bia):
	ano += 1
	altura_bia += taxa_bia
	alt += taxa
print(ano)