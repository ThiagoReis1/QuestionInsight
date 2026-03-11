n1 = int(input("Primeiro numero: "))
n2 = int(input("Segundo numero: "))
n3 = int(input("Terceiro numero: "))

if n1%2 == 0:
	a = 1
else:
	a = 0
	
if n2%2 == 0:
	b = 1
else:
	b = 0
	
if n3%2 == 0:
	c = 1
else:
	c = 0
	
if a+b+c>=2:
	print("SIM")
else:
	print("NAO")