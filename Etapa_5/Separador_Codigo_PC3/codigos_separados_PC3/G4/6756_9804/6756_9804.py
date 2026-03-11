# faça seu código aqui!
q = int(input())

if q == 15:
	t = 16.00
elif q < 15:
	t = 20.00
else:
	t = 10.00
	
x = (175 * q) + t

print(round(x,2))