altura_joe = 1.77
taxa_joe = 0.02
anos = 0

alturap = float(input("insira uma altura:"))
taxap = float(input("insira uma taxa:"))

while (alturap<altura_joe):
	alturap = alturap +taxap
	altura_joe = altura_joe + taxa_joe
	anos = anos +1
	
print(anos)