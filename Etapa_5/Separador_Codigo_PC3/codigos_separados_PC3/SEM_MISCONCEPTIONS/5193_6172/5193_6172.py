a = float(input())
b = float(input())
c = float(input())
d = float(input())

valor = a*7.00 + b*6.00 + c*3.00 + d*5.00

if valor <= 42.00:
	total = valor - 3
	print(round(total,2),'ryous')
else:
	total = valor - (valor*0.10)
	print(round(total,2),'ryous')