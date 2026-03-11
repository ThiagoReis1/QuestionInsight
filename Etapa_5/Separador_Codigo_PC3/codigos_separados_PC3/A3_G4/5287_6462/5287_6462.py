k = input("").upper()
c = 0 
i = 0
while (k == "COROA" or k == "CARA" or k== "S"):
	i = i + 1
	if k == "CARA":
		c = c + 1
	perc = (c/i)*100
	if k == "S":
		print(i-1)
		print(round(((c/(i-1))*100) , 2))
		break
	k = input("").upper()