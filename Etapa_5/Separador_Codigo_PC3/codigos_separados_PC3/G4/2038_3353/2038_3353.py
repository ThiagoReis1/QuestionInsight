r=(input("resposta: "))

sim=0
nao=0

while(r.upper()!="S"):
	if(r.upper()=="SIM"):		
		sim=sim+1
	else:
		nao=nao+1
	r=(input("resposta: "))
		
		
print(sim)