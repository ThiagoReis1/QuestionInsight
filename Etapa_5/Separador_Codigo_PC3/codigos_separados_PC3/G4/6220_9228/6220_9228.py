x = int(input("digite o valor de x"))
y = int(input("digite o valor de y"))

cont = x
acum = 0

while cont <= y:
	if cont%3 == 0:
		acum = acum + cont
	cont = cont + 1
print(acum)