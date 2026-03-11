prod = input("Produto: ").upper()
i=0
tot=0

while i < len(prod):
	if prod[i]=="D":
		tot += 2.25
	if prod[i]=="S":
		tot += 4
	if prod[i]=="I":
		tot += 6.9
	i+=1	

print(round(tot,2))

