a=float(input("deposito inicial"))
b=(int(input("meses")))
c=0
cont=1

while(cont+1):
	juros=(0.01*a)*cont
	total=(a+juros)
	
print(round(total,2))