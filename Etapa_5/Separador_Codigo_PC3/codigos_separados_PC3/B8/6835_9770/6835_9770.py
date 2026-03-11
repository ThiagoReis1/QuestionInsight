compras = input()
i =0
total = 0 
while i< len(compras):
	if compras[i]=="B":
		total+= 3.75
	elif compras[i]=="C":
		total+= 7.90
	elif compras[i]=="E":
		total+= 9.85
	i+=1
print(round(total,2))
