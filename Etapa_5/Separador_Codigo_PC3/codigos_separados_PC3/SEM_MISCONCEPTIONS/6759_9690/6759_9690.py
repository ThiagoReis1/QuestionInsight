# faça seu código aqui!
d = int(input("distancia da entrega: "))

if d==10:
	total = 50 + 7.75
elif d<10:
	total= 50 + 5.50
else:
	total = 60
	
print(round(total,2))