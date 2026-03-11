p = int(input("Insira um numero de 1 a 4 referente ao prato: "))
s = int(input("Insira um numero de 1 a 4 para sobremesa: "))
b = int(input("Insira um numero de 1 a 4 para bebida: "))

m = (p >= 1) and (p <= 4)
n = (s >= 1) and (s <= 4)
o = (b >= 1) and (b <= 4)

if p == 1:
	x = 180
elif p == 2:
	x = 230
elif p == 3:
	x = 250
else:
	x = 350
if s == 1:
	y = 75
elif s== 2:
	y = 110
elif s == 3:
	y = 170
else:
	y = 200
if b == 1:
	z = 20
elif b == 2:
	z = 70
elif b == 3:
	z = 100
else:
	z = 65

c = x + y + z

if m and n and o:
	c
	print("Calorias:", c,"cal")
else:
	print("Dados invalidos")
		