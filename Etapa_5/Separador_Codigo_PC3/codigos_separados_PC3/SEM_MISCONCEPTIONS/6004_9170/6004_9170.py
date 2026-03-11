tm = int(input("Quantidade de Tomates:"))

if tm < 4:
	total = tm*0.75
	
else:
	total = tm*0.55
	
print(round(total,2))