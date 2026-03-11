num = int (input("Digite um numero inteiro: "))

if (num % 23 == 0):
	print (int(num/23))
	print ("sim")
else:
	print (int(num % 23))
	print ("nao")