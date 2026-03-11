cons = float(input("Energia eletrica: "))

if(cons > 150):
	cobra = (0.75*cons) + 16.00
else:
	cobra = (0.60*cons) + 5.00
print(round(cobra,2))
	