altura_joe = 1.77
taxa_joe = 0.02

alt_pessoa = float(input('altura da pessoa: '))
tx = float(input('taxa de crescimento: '))

anos = 0

while (alt_pessoa < altura_joe):
	altura_joe += taxa_joe
	alt_pessoa += tx
	
	anos += 1
	
print(anos)