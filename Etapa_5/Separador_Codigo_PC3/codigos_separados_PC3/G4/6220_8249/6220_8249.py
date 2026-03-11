x = int(input())
y = int(input())

acum = 0
cont = x
while cont <= y:
	if cont % 3 == 0:
		acum = cont + acum
	cont = cont + 1

print(acum)
		
		
