num = int(input("Diga o valor: "))

cont = 0

while (num >= 0):
	if (num >= 101) and (num <= 201):	
		cont = cont + 1
		
	num = int(input("Diga o valor: "))

print(cont)
