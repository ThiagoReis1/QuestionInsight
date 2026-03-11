n = int(input("digite um numero:"))
n1 = n // 100
n2 = n % 100
if (n == (n1 + n2)**2):
   print(n,"atende a propriedade") 
else:
	x = (n1 + n2)**2
	print(x)