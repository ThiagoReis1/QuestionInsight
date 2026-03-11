x = float(input("valor do numero"))
y = (x // 10000)
z = ((x % 10000) // 100)
w = (z%100)
if(x == y**3 + z**3 + w**3):
	print("X atende a propriedade")
else:
	print(y**3 + z**3 + w**3)