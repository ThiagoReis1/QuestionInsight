altura_chico = 1.5
taxa_chico = 0.02
altura_p = float(input(" "))
taxa_c =float(input(" "))

anos = 0

while altura_p < altura_chico:
	altura_p += taxa_c
	altura_chico += taxa_chico
	
	anos = anos + 1
print(anos)

