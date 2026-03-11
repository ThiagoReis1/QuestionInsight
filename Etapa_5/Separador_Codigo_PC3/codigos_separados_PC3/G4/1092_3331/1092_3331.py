num=int(input("valor: "))
n1= num // 100
n2= (num % 100)// 10
n3= (num % 10)

c=(n1**3) + (n2**3) + (n3**3) 

if(c == num):
	print(num)
	print("atende")
else:
	print(num)
	print("nao atende")