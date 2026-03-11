p=float(input("Qual peso da sua encomenda?"))
if(p<=4999.9):
	preco=0.05*p
else:
	preco=(0.04*p)+60.00
print(round(preco,2))