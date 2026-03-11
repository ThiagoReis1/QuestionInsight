# faça seu código aqui!
diaria = 100
dias = int(input(''))

if dias <7 :
	total = diaria * dias + 15
	
elif dias == 7 :
 	total = diaria * dias + 12
else:
	total = diaria * dias + 10
	
print(round(total,2))