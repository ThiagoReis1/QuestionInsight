p = int(input("prato: "))
s = int(input("sobremesa: "))
b = int(input("bebida: "))

if ((p < 1) and (p > 4)) or ((s < 1) and (s > 4)) or ((b < 1) and (b > 4)):
   print("Dados invalidos")
else:
	if (p == 1):
	c = 180
elif (p == 2):
   c = 230
elif (p == 3):
	c = 250
else:
	c = 350
if (s == 1):
	d = 75
elif (s == 2):
	d = 110
elif (s == 3):
	d = 170
else:
	d = 200
if (b == 1):
	e = 20
elif (b == 2):
	e = 70
elif (b == 3):
	e = 100
else:
	e = 65

x = c + d + e
print("Calorias: ", x, "cal")