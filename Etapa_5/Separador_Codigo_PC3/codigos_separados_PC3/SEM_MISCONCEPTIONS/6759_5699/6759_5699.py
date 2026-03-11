distancia = int(input())
custo = 50.0

if distancia<10:
	custo += 5.5
elif distancia==10:
	custo += 7.75
else:
	custo += 10

print(round(custo,2))
