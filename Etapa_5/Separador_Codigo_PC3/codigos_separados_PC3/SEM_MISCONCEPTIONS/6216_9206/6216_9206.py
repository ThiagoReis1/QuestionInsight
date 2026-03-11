x = int(input("Determine o valor de x:"))
y = int(input("Determine o valor de y:"))

num = x
while num >= 0:
	if num % 5 == 0:
		soma = soma + num
	   num = soma
print(x , y)