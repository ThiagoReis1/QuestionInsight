# faça seu código aqui!
d = int(input("distancia da entrega:"))

if d < 10:
	valor = 50 + 5.5
elif d == 10:
	valor = 50 + 7.75
else:
	valor = 50 + 10
print(valor)
