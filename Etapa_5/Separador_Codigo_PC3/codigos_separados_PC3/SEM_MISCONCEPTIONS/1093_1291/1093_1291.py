num = int(input("digite o valor do numero"))
valor1 = num % 2
valor2=  num % 10
valor3= num % 100
calc = valor2**2 + valor3**2


if(valor1 != 0):
	print("X atende as condiçoes")


else: 
	print(calc )
	