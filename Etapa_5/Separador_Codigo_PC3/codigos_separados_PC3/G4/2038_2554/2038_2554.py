sats=input("atendimento satisfatorio?, digite sim ou nao: ").upper()
cli=0
while(sats!="S"):
	if(sats=="SIM"):
		sats=input("atendimento satisfatorio?, digite sim ou nao: ").upper()
		cli=cli+1
	else:
		sats=input("atendimento satisfatorio?, digite sim ou nao: ").upper()
print(cli)
	 
	