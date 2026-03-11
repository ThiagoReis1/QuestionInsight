# faça seu código aqui!
d = int(input())

total = 50


if d < 10:
	total+=5.5
elif d > 10:
	total+=10
else:
	total+=7.75
	
print(round(total,2))