# faça seu código aqui!
d = int(input("Insira aqui a distancia da entrega em km: "))

ini = 50.0

if d < 10:
	x = 5.5 + ini
elif d == 10:
	x = 7.75 + ini
else:
	x = 10.0 + ini
	
round(x, 2)
print(x)