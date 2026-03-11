achico = 1.5
tchico = 0.02
alt = float(input("alt da garela: "))
tx = float(input("tx de cresc: "))
anos = 0

while  achico > alt:
	alt = alt + tx
	achico = achico + tchico
	anos = anos + 1
	
print(anos)