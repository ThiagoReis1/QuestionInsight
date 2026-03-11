altura_joe = 1.77
taxa_joe = 0.02

altura = float(input("insira um numero: "))
taxa = float(input("insira um numero: "))

ano=0

while altura < altura_joe:
	altura_joe = altura_joe + taxa_joe
	altura = altura + taxa
	ano += 1 
print(ano)