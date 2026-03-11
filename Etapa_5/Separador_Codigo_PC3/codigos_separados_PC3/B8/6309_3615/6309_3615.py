vet = input()

i = 0
total = 0.0
qtd_h = 0
qtd_c = 0
qtd_l = 0
while i < len(vet):
	if vet[i] == "H":
		total +=5.4
		qtd_h +=1
	elif vet[i] == "C":
		total +=8.95
		qtd_c +=1
	elif vet[i] == "L":
		total += 4.5
		qtd_l +=1
	i+=1
print(round(total,2), qtd_h, qtd_c, qtd_l)