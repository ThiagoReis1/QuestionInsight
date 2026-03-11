x = input("Digite a cor: ")
x = x.upper()
i=0
while(x!="S"):
	x = x.upper()
	if(x=="PRETA"):
		i = i + 1
		x = input("Digite a cor: ")
		x = x.upper()
	else:
		x = input("Digite a cor: ")
		x = x.upper()
print(i)
	
	