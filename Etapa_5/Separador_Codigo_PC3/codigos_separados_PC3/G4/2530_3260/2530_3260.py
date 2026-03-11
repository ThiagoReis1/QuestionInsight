d= float(input("deposito inicial= "))
t = float(input("tarifa fixa= "))
j = float(input("taxa de juros= "))

df = d + (d * 0.15)
j = j/100
n = 0

if d > 0 and t > 0 and j > 0:
	while d < df:
		d = (d + (d * j)) - t
		round(d ,2)
		n = n + 1
	print(n)
else :
	print("Dados incorretos")