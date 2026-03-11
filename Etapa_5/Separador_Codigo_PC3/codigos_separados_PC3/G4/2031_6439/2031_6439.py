face = int(input("entre com valor para face: "))
cont = 0

while (face != -1):
	if (face == 6):
		cont = cont + 1
	face = int(input('entre com um novo valor para face: '))
print(cont)