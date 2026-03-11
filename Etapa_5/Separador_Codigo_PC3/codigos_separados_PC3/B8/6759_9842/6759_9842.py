valor = int(input(""))

if(valor < 10):
	varia = 5.5
else:
	if(valor == 10):
		varia = 7.75
	else:	
		if(valor > 10):
			varia = 10.0

total = 50.0 + varia
	
print(round(total, 2))