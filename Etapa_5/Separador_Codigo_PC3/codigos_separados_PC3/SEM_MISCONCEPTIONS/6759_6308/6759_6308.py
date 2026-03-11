distancia = int(input())

if(distancia < 10):
	total = 50 + 5.5
elif(distancia == 10):
	total = 50 + 7.75
else:
	total = 50 + 10

print(round(total,2))