peso = float(input(""))
quantidade = float(input(""))

for i in range(4):
	peso = peso - quantidade
	i = i + 1

print("{:.2f}".format(peso))