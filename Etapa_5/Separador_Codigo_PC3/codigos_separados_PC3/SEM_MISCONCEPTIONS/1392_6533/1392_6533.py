ca = float(input("inserir consumo de agua: "))

taxa = 30.0

if(ca < 10):
	total= (3.0 * ca) + taxa

else: 
	total= (3.50 * ca) + taxa
print(round(total, 20))