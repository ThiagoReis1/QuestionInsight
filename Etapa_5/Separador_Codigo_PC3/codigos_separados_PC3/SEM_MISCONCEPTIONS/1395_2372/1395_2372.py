vendas = float(input())
a = 0.05 * vendas 
b = vendas % 1000
c = (vendas - b) - (vendas // 1000) * 1000
d = 0.05 * c
e = 
f = d + e
if(vendas <= 1000):
	print(round(a, 2))
else:
	print(round(f, 2))