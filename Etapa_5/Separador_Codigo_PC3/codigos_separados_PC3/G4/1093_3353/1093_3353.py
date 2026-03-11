num=int(input("digite um numero: "))
a=num//100
b=(num%100)

if(num==(a**2+b**2)):
	print("atende")
	print(num)
else:
	print("nao atende")
	print(num)