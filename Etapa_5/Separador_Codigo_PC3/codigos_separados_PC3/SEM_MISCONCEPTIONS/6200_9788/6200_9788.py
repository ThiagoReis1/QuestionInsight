altura_max = 1.75
taxa_max = 0.01

altura_colega = float(input())
taxa_colega = float(input())

ano = 0 

while (altura_max > altura_colega):
	
	altura_max = altura_max + taxa_max
	
	altura_colega = altura_colega + taxa_colega
	
	ano += 1
	
print(ano)