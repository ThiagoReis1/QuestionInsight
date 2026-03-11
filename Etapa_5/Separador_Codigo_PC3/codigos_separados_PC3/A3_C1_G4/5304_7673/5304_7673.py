b = int(input())
h = float(input())

bac = 1
hora = 1

while(h > 0):
	bac = bac + b
	hora = bac + (15/100) * bac
	
	int(input(hora))
	if(h<=0):
		print(hora)
	

