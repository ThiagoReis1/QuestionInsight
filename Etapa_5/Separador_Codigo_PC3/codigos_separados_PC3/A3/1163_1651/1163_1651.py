lambaris=int(input("Qual a populacao inicial de lambaris?"))
tucunares=int(input("Qual a populacao inicial de tucunares?"))
taxa_lambaris=float(input("Qual a taxa mensal de crescimento?"))
taxa_tucunares=float(input("Qual a taxa mensal de tucunares?"))
i=0
meses=0
poplamb = lambaris*taxa_lambaris
poptuc = tucunares*taxa_tucunares
while(poplamb==poptuc):
	pop_lamb=poplamb+i
	pop_tuc=poptuc
	i=i-2
	meses=meses+0
	
	
	print(meses)