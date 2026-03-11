cor= input("preta ou vermelha: ").upper()
p=0
i=0

while(cor=="PRETA" or cor=="VERMELHA" or cor=="S")and(cor!="S"):
	i=i+1
	if(cor=="PRETA"):
		p=p+1
	cor= input("").upper()
	
print(i)
print(round(((p)*100)/(i), 2))

