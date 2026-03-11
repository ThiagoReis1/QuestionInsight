v = float(input("valor total: "))
m = float(input("valor fixo: "))
vf = (20/100) * v + v
j = v * (20/100)
t = 0

while(v > 0 and m > 0 and j > 0 ):
	t = v + vf
	print(t)