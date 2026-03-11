num = int(input("informe o valor"))

a = num // 1000
b = num % 1000

x = (a-b)**2
if (num == x ):
	print("atende")
else:
	print("nao atende")
print(num)