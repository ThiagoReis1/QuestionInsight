produto = input ("digite uma letra: ").upper()

i= 0
valor_total = 0
qtd_mercearia = 0
qtd_padaria = 0
qtd_rotisseria = 0

while i < len (produto):
	if produto [i] == "M":
		valor_total += 7.25
		qtd_mercearia += 1
	elif produto [i] == "P":
		valor_total += 4.75
		qtd_padaria += 1
	elif produto [i] == "R":
		valor_total += 3.50
		qtd_rotisseria += 1 
	i += 1
print (round (valor_total, 2))