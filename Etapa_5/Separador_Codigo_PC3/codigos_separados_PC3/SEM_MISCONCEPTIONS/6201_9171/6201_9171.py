altura_joe = 1.77
taxa_joe = 0.02

alt = float(input())
taxa = float(input())

ano = 0

while alt < altura_joe:
	alt = alt + taxa
	altura_joe = altura_joe + taxa_joe
	ano = ano + 1
	
print(ano)