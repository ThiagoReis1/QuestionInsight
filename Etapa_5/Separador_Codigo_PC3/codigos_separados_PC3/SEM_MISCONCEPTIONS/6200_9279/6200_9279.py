altura_max = 1.75
taxa_max = 0.01
altura = float(input('altura'))
taxa = float(input('taxa'))
ano = 0
while(altura_max > altura):
	altura = altura + taxa
	altura_max = altura_max + taxa_max
	ano = ano + 1
print(ano)