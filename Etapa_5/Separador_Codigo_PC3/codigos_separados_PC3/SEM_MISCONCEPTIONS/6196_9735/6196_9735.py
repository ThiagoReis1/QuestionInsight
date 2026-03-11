altura_chico = 1.5
taxa_chico = 0.02

alh = float(input("Altura h: "))
taxah = float(input("Taxa h: "))
anos = 0

while alh<altura_chico:
	anos = anos + 1
	altura_chico = altura_chico + taxa_chico
	alh = alh + taxah
print(anos)
	
