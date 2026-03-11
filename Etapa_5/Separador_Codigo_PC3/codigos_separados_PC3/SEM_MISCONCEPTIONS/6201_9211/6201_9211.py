altura_eve = float(input("digite a altura da eve"))
taxa_eve = float(input("escreva a taxa da eve"))
altura_joe = 1.77
taxa_joe = 0.02
anos = 0
while altura_joe > altura_eve :
	altura_eve = altura_eve + taxa_eve
	altura_joe = altura_joe + taxa_joe
	anos = anos + 1
print(anos)