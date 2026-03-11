x = int(input("Digite o numero: "))
y = (x//100)
z = (x%100)
k = (y**2 + z**2)
print(k)
if(k == x):
	print("x atende a propriedade")