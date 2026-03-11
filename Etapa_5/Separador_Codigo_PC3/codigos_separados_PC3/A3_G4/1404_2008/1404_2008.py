n = input("nome da cabeça: ")
d1 = int(input("valor do dado 1: "))
d2 = int(input("valor do dado 2: "))
d3 = int(input("valor do dado 3: "))

da1 = d1 + d2 + d3
da2 = 2 * (d1 + d2 + d3)

if (n == da1):
	da1 = d1 + d2 + d3
	
	print(da1)
	
else:
	da2 = 2 * (d1 + d2 + d3)
	print(da2)