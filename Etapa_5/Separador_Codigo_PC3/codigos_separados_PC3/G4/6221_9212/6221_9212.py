x = int(input("digite o valor de x:"))
y = int(input("digite o valor de y:"))

soma = 0
num = x
while num <= y:
	if num % 7 == 0:
		soma = soma + num
	num = num + 1
print(soma)