altura_joe = 1.77
taxa_joe = 0.02

anos = 0

altura = float(input("Altura: "))
taxa = float(input("Taxa: "))

while altura_joe > altura:
	altura_joe = altura_joe + taxa_joe
	altura = altura + taxa
	anos = anos + 1

print(anos)
