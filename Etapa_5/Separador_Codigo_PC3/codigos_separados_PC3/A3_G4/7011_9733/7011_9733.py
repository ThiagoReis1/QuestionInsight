x = int(input("Digite o X:"))
y = int(input("Digite o Y:"))

cont = 0
num = x

while num <= y:
	if num % 5 ==0:
		print(num)
	num = num + 1
