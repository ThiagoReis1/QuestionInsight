num= int(input("Digite um numero de 4 digitos: "))

d1= num // 100
d2= num % 100

c= (d1 ** 2) + (d2 ** 2)

if( c == num):
	print("atende")
	print(num)
else:
	print("nao atende")
	print(num)