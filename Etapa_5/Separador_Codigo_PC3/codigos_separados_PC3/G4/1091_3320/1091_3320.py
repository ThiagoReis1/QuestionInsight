num = int(input("numero fornecido:"))
a= num //100
b = num % 100

if(num==(a+b)**2):
	print(num, "atende")
else:
	print(num, "nao atende")