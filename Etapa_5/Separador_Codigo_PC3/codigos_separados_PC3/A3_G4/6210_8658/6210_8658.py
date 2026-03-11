x = int(input(""))
cont = 0
soma = 0
while x > -1:
	if x >= 35 and x <= 95:
		x = x + 1
		cont = cont + x
	x = int(input(""))
	
	if x == -1:
		x = x + 1 
		soma = cont + 1
		
		
print(soma)	