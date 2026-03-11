nume = int(input("qual: "))

#primeira parte
a = nume // 100

#resto
resto_de_a = nume % 100

#segunda parte
b = resto_de_a // 1

calculo = (a + b) ** 2

if (calculo == nume):
	mensag = ("atende")
	
else:
	mensag = ("nao atende")

print(nume)
print(mensag)