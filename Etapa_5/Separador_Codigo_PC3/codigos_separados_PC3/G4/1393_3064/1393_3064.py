peso= float(input("informe o peso da encomenda em gramas: "))
if peso>=5000:
	x= ((peso)*0.04)+60
else:
	x=(peso)*0.05
print(round(x,2))	