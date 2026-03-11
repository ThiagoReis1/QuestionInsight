#pesquisa de satisfacao

resp=input("Digite a resposta:").upper()

cont=0
conts=0

while (resp!="S"):
	if (resp=="SIM"):
		conts= conts+1
		resp=input("Digite a resposta:").upper()
		cont=cont+1
		
	else:
		cont=cont+1
		resp=input("digite a resposta:").upper()

tax=(conts/cont)*100		
print(cont)
print(tax)
		
		