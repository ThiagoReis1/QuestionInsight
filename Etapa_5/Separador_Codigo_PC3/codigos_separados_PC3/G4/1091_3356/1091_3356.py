n = int(input())

a = (n -(n % 100)) //100
b = (n-(n -(n % 100)))

cal = (a + b)**2


if (n == cal):
	print (n)
	print ("atende")
else :
	print (n)
	print ("nao atende")