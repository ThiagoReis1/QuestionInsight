num= int(input("Digite um numero:"))
p1= num // 100
p2= num % 100

if ((num == (p1 ** 2) + (p2 ** 2))):
	 print("atende")
	 print(num)
else:
	 print("nao atende")
	 print(num)