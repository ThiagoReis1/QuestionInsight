altura_joe = 1.77
taxa_joe = 0.02
aj = altura_joe
tj = taxa_joe
altura = float(input())
taxa = float(input())
anos = 0

while altura < aj:
	aj = aj + 0.02
	altura = altura + taxa
	anos = anos + 1
print(anos)


