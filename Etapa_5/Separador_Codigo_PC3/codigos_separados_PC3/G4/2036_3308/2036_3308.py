x = input("digite a cor da bolinha:").upper()

qtdp = 0
while(x!="S"):
	if(x == "PRETA"):
		qtdp = qtdp + 1
		x = input("digite a cor da bolinha:").upper()	
	else:
		x = input("digite a cor da bolinha:").upper()	
print(qtdp)	
	