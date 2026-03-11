
pr = input("Digite a inicial dos Produtos: ").upper()
total = 0
i=0
while i < len(pr):
	if pr[i] == "D":
		total+=2.25
	elif pr[i]=="S":
		total+=4
	elif pr[i]=="I":
		total+=6.9
	i+=1
print(round(total,2))

