num = int(input("Digite um numero: "))

num1 = num // 10000

num2 = (num % 10000) // 100

num3 = (num % 10000) % 100

t = (num1 ** 3) + (num2 ** 3) + (num3**3)

if(t == num):
	print("atende")
	print(num)
else:
	print("nao atende")
	print(num)

