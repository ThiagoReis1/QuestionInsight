x = int(input("qual o valor: "))
a = x // 100
b = (x%100) // 10
c = (x%100)%10
y = a**3 + b**3 + c**3
print(x)
if (y == x):
	print("atende")
else:
	print("nao atende")