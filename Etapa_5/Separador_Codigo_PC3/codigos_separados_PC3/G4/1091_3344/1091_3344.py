a = int(input("Digite aqui: "))

b = a//100
c = a%100


conta3 = (b + c)**2

if( conta3 == a ):
	print(a)
	print("atende")
else:
	print(a)
	print("nao atende")