x = int(input("Digite um numero: "))

if (x % 47 == 0):
	q = x//47
	print(round(q, 0))
	print ("sim")

	
else:
	resto = x % 47
	print(round(resto, 0))
	print ("nao")
	

	
