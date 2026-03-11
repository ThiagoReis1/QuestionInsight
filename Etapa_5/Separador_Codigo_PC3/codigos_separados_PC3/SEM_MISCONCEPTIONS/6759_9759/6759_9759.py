# faça seu código aqui!
dist = int(input("Informe a distancia em km: "))

if dist < 10:
	total = 50 + 5.5 
	print(round(total, 2))
elif dist == 10:
	total = 50 + 7.75
	print(round(total,2 ))
else: 
	total = 50 + 10
	print(round(total, 2))