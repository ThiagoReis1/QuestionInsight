num = int(input("numero:"))
a = num // 10000
b = (num % 10000) 
print(num)
if (num  == (a + b)**2 ):
	print("atende")
else:
	print("nao atende")