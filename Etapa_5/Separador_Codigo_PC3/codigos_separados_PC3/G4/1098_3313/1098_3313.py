num = int(input("insira o numero: "))
d1 = num // 1000
d2 = num % 1000
x = (d1 - d2)**4
print(num)
if(num == x):
	print("atende")
else:
	print("nao atende")
