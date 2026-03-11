n = int(input(":"))
cont = 0
cont2 = 0
por = 0

while n != 0:
	cont = cont + 1
	if n % 3 == 0:
		cont2 += 1
		
	n = int(input(":"))
	
por = (cont2 * 100) / cont
print(cont)
print(round(por,2))