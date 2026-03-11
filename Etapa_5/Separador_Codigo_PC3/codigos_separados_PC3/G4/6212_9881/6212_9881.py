l = int(input("n medico: "))

cont = 0

while l != -1: 
	if l >= 26 and l <= 85:
		cont = cont + 1
	l = int(input("n medico: "))
	
print(cont)