produtos =input("digite os produtos (B)biscoito , (C)cereais e (E)enlatados: ").upper()

total= 0
i = 0 
cont_b=0
cont_c=0
cont_e=0

while i < len(produtos):
	if produtos[i] == "B":
		total = total + 3.75
		cont_b = cont_b + 1
	elif produtos[i] == "C":
		total = total + 7.9
		cont_c += 1
	elif produtos[i] == "E":
		total = total + 9.85
		cont_e += 1
	i += 1
print(round(total, 2))