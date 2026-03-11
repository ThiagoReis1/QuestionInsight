pl=int(input("Digite a população:"))
pt=int(input("Digite a população:"))
tl=float(input("Digite a taxa mensal:"))
tt=float(input("Digite a taxa mensal:"))
meses=1
tl=tl+1
tt=tt+1
while(pl>pt):
	pl=pl*tl
	pl=pl-(2*pt)
	pt=pt*tt
	meses=meses+1
print(meses)
	
	
	