a= input("SIM OU NAO:").upper()
sim=0
nao=0
while(a!="S".upper()):
	if(a=="SIM".upper()):
		sim=sim+1
		a=input("SIM OU NAO: ").upper()
	if(a=="NAO".upper()):
		nao=nao+1
		a=input("SIM OU NAO: ").upper()
total=sim+nao
pct=sim*100/total
print(total)
print(round(pct,2))