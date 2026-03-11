face = input("Informe a face da moeda: ").upper()
i=0

while face != "S":
	if face == "CARA":
		i=i+1
	face = input("Informe a face da moeda: ").upper()
	
print(i)