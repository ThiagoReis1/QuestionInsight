hora = int(input())
pratos = float(input())
total = pratos*28.50

if(hora>=18):
	total = total -(total*0.2)
	print(round(total,2))
else:
	print(round(total,2))
	
	