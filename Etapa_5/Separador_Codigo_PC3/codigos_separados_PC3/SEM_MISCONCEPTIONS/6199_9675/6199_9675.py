altura_cicero = 1.8
taxa_cicero = 0.01

pessoa_altura = float(input())
pessoa_taxa = float(input())

anos = 0

while pessoa_altura <= altura_cicero:
	altura_cicero += taxa_cicero
	pessoa_altura += pessoa_taxa
	anos = anos + 1
print(anos)