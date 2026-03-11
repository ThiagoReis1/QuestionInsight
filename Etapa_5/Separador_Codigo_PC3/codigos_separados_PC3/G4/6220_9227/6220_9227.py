x = int(input("numero de x:"))
y = int(input("numero de y:"))
cont = x
acum = 0
while cont <= y:
	if cont%3 == 0:
		acum = acum + cont
	cont = cont + 1
print(acum)