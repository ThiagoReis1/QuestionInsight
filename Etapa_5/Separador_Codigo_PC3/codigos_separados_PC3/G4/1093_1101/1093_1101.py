x = int(input("Digite o número: "))

w = x // 1000 
y = x % 1000
z = (w + y)**2

if (x == z):
	print("X atende a propriedade")
else:
	print(z)
	
	