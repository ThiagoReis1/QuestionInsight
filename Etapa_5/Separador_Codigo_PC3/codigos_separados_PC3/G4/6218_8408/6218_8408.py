x = int(input("valor x: "))
y = int(input("valor y: "))
i=x
soma = 0

while(i <= y):
	if(i %2 == 0):
		soma = soma+i
		print(i)
	i= i+1