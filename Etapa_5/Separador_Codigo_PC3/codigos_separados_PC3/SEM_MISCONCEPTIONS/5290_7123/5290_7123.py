face = int(input("faces:"))
cont = 0
total = 0
while (face != -1):
	if (face == 5):
		cont = cont + 1
	total = total + 1
	face = int(input("faces:"))
	
total2 = 100 * cont / total
print(total)
print(total2)