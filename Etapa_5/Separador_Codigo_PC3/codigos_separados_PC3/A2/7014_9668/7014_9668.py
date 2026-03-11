num_x = int(input("valor de x: "))
num_y = int(input("valor de y: "))

soma= 0

while ( num_x <= num_y):
	if num_x % 2 == 0:
		soma = soma 
		num_x = num_x + 1
	else:
		soma= soma + num_x
		num_x = num_x + 1
print (soma)