c = float(input())
d = float(input())
m = float(input())
j = float(input())

j = j/100

mes = 0

if c<=0 or d<=0 or m<=0 or j<=0 :
	print("Dados incorretos")
else:
	while (d < c):
		d = d + d*j
		d = d + m
		d = round(d,2)
		mes = mes + 1
	print(mes)