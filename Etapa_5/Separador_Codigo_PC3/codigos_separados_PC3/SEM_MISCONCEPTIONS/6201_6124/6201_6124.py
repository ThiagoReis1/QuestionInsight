altura_joe = 1.77
taxa_joe = 0.02

alt = float(input("Altura de uma pessoa: "))
taxa = float(input("Taxa de crescimento: "))
ano = 0

while alt < altura_joe:
	altura_joe = altura_joe + taxa_joe
	alt = alt + taxa
	ano = ano + 1
print(ano)