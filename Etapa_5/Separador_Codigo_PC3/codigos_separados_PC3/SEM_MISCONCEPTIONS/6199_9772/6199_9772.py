altura_cicero = 1.8
taxa_cicero = 0.01

alt = float(input(''))
taxa = float(input(''))

ano = 0

while (alt < altura_cicero):
	ano += 1 
	altura_cicero += taxa_cicero
	alt += taxa 

print(ano)