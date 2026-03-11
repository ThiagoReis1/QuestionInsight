cor=input("preta ou vermelha: ").upper()
cont=0

while(cor!="S"):
	if(cor=="PRETA"):
		cont=cont+1
	cor=input("preta ou vermelha: ").upper()
print(cont)