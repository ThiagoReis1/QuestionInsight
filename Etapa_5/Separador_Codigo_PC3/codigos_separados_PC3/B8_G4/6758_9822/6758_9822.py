# faça seu código aqui!
x = int(input())

d = 100.00

if x < 7:
	tt = (d*x) + 15.00
elif x == 7:
	tt = (d*x) + 12.00
elif x > 7:
	tt = (d*x) + 10.00
print(round(tt,2))