casa=input("Cor da casa:").upper()
som=0
while(casa!="S"):
	if(casa=="PRETA"):
		som=som+1
		casa=input("Cor da casa:").upper()
	else:
		casa=input("Cor da casa:").upper()
print(som)
		