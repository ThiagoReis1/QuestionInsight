from math import factorial

num_x = float(input("De um valor real a X: "))
num_k = int(input("Quantos numeros tera a serie de Maclaurin? "))

count_k = 0
result = 0

while count_k < num_k:
	result += (num_x**count_k)/factorial(count_k)
	count_k += 1
	
print(round(result, 9))
