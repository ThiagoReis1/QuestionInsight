a = int(input("Numero: "))

b = a//100
c = a%100
d = (b + c)**2

print(a)

if (a == d):
	print("atende")
else:
	print("nao atende")