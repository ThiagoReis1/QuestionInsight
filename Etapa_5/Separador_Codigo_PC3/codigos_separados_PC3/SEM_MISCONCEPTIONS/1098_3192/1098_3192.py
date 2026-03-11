num = int(input("digite um numero: "))

valor1 = num // 1000
resto1 = num % 1000

calculo = (valor1 - resto1)**4

if (calculo == num):
	print(num)
	print("atende")
	
else: 
	print(num)
	print("nao atende")
	
	