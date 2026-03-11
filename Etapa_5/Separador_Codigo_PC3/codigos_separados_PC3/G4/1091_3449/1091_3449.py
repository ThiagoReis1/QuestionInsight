num=int(input("numero: "))
d1=num//100
d2=num%100


calculo= ((d1+d2)**2)

if	(calculo==num):
	print(num)
	print("atende")
else:
	print(num)
	print("nao atende")