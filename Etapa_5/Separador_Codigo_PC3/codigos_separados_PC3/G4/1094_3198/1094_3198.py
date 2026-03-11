num = int(input())


d1 = num // 1000
d2 = num % 1000

if (d1 + d2)**2 == num:
	print("atende" , num)
	
else:
	print("nao atende" ,  num)






