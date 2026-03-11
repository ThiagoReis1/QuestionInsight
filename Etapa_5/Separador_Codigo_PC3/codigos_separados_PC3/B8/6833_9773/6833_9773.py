compras=input()
i=0
total=0
while i < len(compras):
	if compras[i]=='M':
		total+=7.25
	elif compras[i]=='P':
		total+=4.75
	elif compras[i]=='R':
		total+=3.5
	i+=1
print(round(total, 2))