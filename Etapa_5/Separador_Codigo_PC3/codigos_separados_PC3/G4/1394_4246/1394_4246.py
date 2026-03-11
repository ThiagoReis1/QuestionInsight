h = int(input()) #quantidade de horas

x = 50*h
y = 50*20
z = 70*(h - 20)

if(h <= 20):
	print(x)
else:
	print(round(y + z, 2))