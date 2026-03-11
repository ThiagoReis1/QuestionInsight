n = int(input("numero fornecido: "))

cal1= (n//100)
cal2= (n%100)

calculo= (cal1 +cal2) **2

if(calculo==n):
	print(n)
	print("atende")
else:
	print(n)
	print("nao atende")
