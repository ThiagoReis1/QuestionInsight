num = int ( input ( "digite um numero inteiro aqui:"))

res = num % 31

if res == 0:
	res1 = num // 31
	print(res1)
	print ("sim")
	
else:
	res2 = num % 31
	print(res2)
	print("nao")