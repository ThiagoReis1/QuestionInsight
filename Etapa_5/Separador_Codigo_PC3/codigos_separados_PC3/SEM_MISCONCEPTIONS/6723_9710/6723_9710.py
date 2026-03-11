x = int(input("informe o valo:"))
if (x % 19 == 0):
	q = x//19
	print(round(q,0))
	print("sim")
	
else:
	resto = x % 19
	print(round(resto,0))
	print ("nao")
	
	