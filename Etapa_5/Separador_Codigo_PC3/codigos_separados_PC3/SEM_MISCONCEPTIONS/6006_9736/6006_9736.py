batata = int(input("Informe quantas babatas serao: "))

if batata <= 10:
	total = batata * 0.90
	
else: 
	total = batata * 0.75
	
print(round(total, 2))