altura_joe = 1.77
taxa_joe = 0.02

altura_caline = float(input("digite:"))
taxa_caline = float(input("digite:"))

ano = 0

while altura_caline < altura_joe:
	altura_joe = altura_joe + taxa_joe
	altura_caline = altura_caline + taxa_caline
	ano += 1
	
	
print(ano)